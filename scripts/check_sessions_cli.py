#!/usr/bin/env python3
"""
Bale Session Checker CLI (Deduplicated strictly by User ID)
===========================================================
Recursively scans zip archives for Bale (.bale) session files,
extracts the exact user_id, iat, and exp directly from inside each token (NOT by filename),
selects the newest/best session per unique User ID, verifies health live against Bale,
and outputs unique sessions per user.

Usage:
    .venv/bin/python scripts/check_sessions_cli.py "/home/mahan/Downloads/Telegram Desktop/sessions"
    .venv/bin/python scripts/check_sessions_cli.py "/home/mahan/Downloads/ses"
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import contextlib
import io
import json
import os
import re
import sys
import time
import zipfile
from pathlib import Path

# Add project src to path
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from bale import Client  # noqa: E402

JWT_PATTERN = re.compile(rb"eyJ[a-zA-Z0-9_\-]+\.eyJ[a-zA-Z0-9_\-]+\.[a-zA-Z0-9_\-]+")


def parse_jwt(token: str) -> tuple[int | None, int, int]:
    """Extract user_id, iat, exp from JWT token payload."""
    try:
        parts = token.split(".")
        if len(parts) < 2:
            return None, 0, 0
        p = parts[1] + "=" * (-len(parts[1]) % 4)
        payload = json.loads(base64.urlsafe_b64decode(p))
        uid = (
            payload.get("payload", {}).get("user_id")
            or payload.get("user_id")
            or payload.get("uid")
        )
        iat = payload.get("iat", 0)
        exp = payload.get("exp", 0)
        return int(uid) if uid else None, iat, exp
    except Exception:
        return None, 0, 0


def scan_archive(
    data: bytes,
    path_chain: str,
    users_map: dict[int, dict],
    file_counter: list[int],
) -> None:
    """Recursively scan archive data in memory and group strictly by account user_id."""
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            for name in z.namelist():
                content = z.read(name)
                subpath = f"{path_chain} -> {name}"
                if name.endswith((".zip", ".zio", ".zip (1)", ".zip (2)", ".zip (3)")) or content.startswith(b"PK\x03\x04"):
                    scan_archive(content, subpath, users_map, file_counter)
                elif name.endswith(".bale"):
                    file_counter[0] += 1
                    matches = JWT_PATTERN.findall(content)
                    if matches:
                        token = matches[0].decode("ascii")
                        uid, iat, exp = parse_jwt(token)
                        if uid is None:
                            continue

                        if uid not in users_map:
                            users_map[uid] = {
                                "user_id": uid,
                                "sessions": {},  # token -> {iat, exp, sources}
                            }

                        if token not in users_map[uid]["sessions"]:
                            users_map[uid]["sessions"][token] = {
                                "iat": iat,
                                "exp": exp,
                                "sources": [],
                            }
                        users_map[uid]["sessions"][token]["sources"].append(subpath)
    except Exception as e:
        print(f"⚠️  خطا در خواندن آرشیو {path_chain}: {e}", file=sys.stderr)


def extract_accounts_from_dir(target_dir: Path) -> tuple[dict[int, dict], int]:
    users_map: dict[int, dict] = {}
    file_counter = [0]
    zip_files = sorted(target_dir.glob("*.zip"))

    if not zip_files:
        for bpath in target_dir.glob("*.bale"):
            file_counter[0] += 1
            matches = JWT_PATTERN.findall(bpath.read_bytes())
            if matches:
                token = matches[0].decode("ascii")
                uid, iat, exp = parse_jwt(token)
                if uid:
                    if uid not in users_map:
                        users_map[uid] = {"user_id": uid, "sessions": {}}
                    if token not in users_map[uid]["sessions"]:
                        users_map[uid]["sessions"][token] = {"iat": iat, "exp": exp, "sources": []}
                    users_map[uid]["sessions"][token]["sources"].append(bpath.name)

    for zpath in zip_files:
        with open(zpath, "rb") as f:
            scan_archive(f.read(), zpath.name, users_map, file_counter)

    return users_map, file_counter[0]


async def test_user_session(
    sem: asyncio.Semaphore,
    uid: int,
    user_data: dict,
    idx: int,
    total: int,
    delay: float,
    timeout: float,
) -> dict:
    """Tests the tokens for a user (newest first). If any is alive, returns that session."""
    # Sort sessions by newest iat/exp first
    sorted_sessions = sorted(
        user_data["sessions"].items(),
        key=lambda item: (item[1]["iat"], item[1]["exp"]),
        reverse=True,
    )

    async with sem:
        if delay > 0:
            await asyncio.sleep(delay)

        for token, meta in sorted_sessions:
            client = Client(f"{uid}:{token}")
            t0 = time.time()
            try:
                await asyncio.wait_for(client._connect_session(client._session), timeout=timeout)
                user = client.user
                name = getattr(user, "name", "") or ""
                uname = getattr(user, "username", "") or ""
                lat = round(time.time() - t0, 2)
                print(f"✅ [{idx:04d}/{total:04d}] سالم -> UID: {uid:<11} | نام: {name:<22} | یوزرنیم: @{uname or '-'} ({lat}s)")
                return {
                    "status": "alive",
                    "user_id": uid,
                    "name": name,
                    "username": uname,
                    "is_deleted": (name == "Deleted Account"),
                    "session_format": f"{uid}:{token}",
                    "jwt": token,
                    "sources": meta["sources"],
                    "latency_s": lat,
                }
            except Exception as exc:
                err_str = str(exc)
                if "4401" in err_str:
                    continue  # try next token for this user if available
                if isinstance(exc, (asyncio.TimeoutError, TimeoutError)):
                    # brief retry
                    await asyncio.sleep(1.0)
                    try:
                        await asyncio.wait_for(client._connect_session(client._session), timeout=timeout)
                        user = client.user
                        name = getattr(user, "name", "") or ""
                        uname = getattr(user, "username", "") or ""
                        lat = round(time.time() - t0, 2)
                        print(f"✅ [{idx:04d}/{total:04d}] سالم (Retry) -> UID: {uid} | نام: {name}")
                        return {
                            "status": "alive",
                            "user_id": uid,
                            "name": name,
                            "username": uname,
                            "is_deleted": (name == "Deleted Account"),
                            "session_format": f"{uid}:{token}",
                            "jwt": token,
                            "sources": meta["sources"],
                            "latency_s": lat,
                        }
                    except Exception:
                        pass
            finally:
                with contextlib.suppress(Exception):
                    await client.close()

        # If none succeeded
        return {
            "status": "dead",
            "user_id": uid,
        }


async def main():
    parser = argparse.ArgumentParser(description="بررسی سلامت سشن‌های بله با حذف تکراری دقیق بر اساس User ID")
    parser.add_argument("path", nargs="?", default="/home/mahan/Downloads/Telegram Desktop/sessions", help="مسیر پوشه حاوی زیپ‌ها")
    parser.add_argument("-c", "--concurrency", type=int, default=15, help="تعداد درخواست همزمان (پیش‌فرض: 15)")
    parser.add_argument("-d", "--delay", type=float, default=0.03, help="تاخیر بین درخواست‌ها به ثانیه (پیش‌فرض: 0.03)")
    parser.add_argument("-t", "--timeout", type=float, default=7.0, help="تایم‌اوت هر اتصال به ثانیه (پیش‌فرض: 7.0)")
    parser.add_argument("-o", "--output", default="valid_unique_users.json", help="نام فایل خروجی جیسون")
    parser.add_argument("--export-sessions", action="store_true", help="استخراج مستقیم به عنوان فایل‌های sessions/*.session")
    args = parser.parse_args()

    target_dir = Path(args.path).expanduser().resolve()
    if not target_dir.exists():
        print(f"❌ مسیر پیدا نشد: {target_dir}", file=sys.stderr)
        sys.exit(1)

    print("=" * 68)
    print("🔍 در حال استخراج و گروه‌بندی دقیق سشن‌ها بر اساس شناسه کاربری (User ID)...")
    print(f"📁 مسیر: {target_dir}")
    print("=" * 68)

    t_start = time.time()
    users_map, total_files = extract_accounts_from_dir(target_dir)
    total_users = len(users_map)

    multi_count = sum(1 for u in users_map.values() if len(u["sessions"]) > 1)
    total_tokens_count = sum(len(u["sessions"]) for u in users_map.values())

    print(f"📁 کل فایل‌های سشن بررسی‌شده: {total_files:,}")
    print(f"🔑 کل سشن‌های پیدا شده: {total_tokens_count:,}")
    print(f"👤 اکانت‌های یکتا (Unique User IDs): {total_users:,}")
    print(f"🔄 اکانت‌هایی که بیش از یک سشن داشتند: {multi_count:,}")
    print(f"⚙️  هم‌روندی: {args.concurrency} ورکر | تاخیر: {args.delay}s | تایم‌اوت: {args.timeout}s")
    print("-" * 68)

    if total_users == 0:
        print("هیچ اکانتی برای بررسی یافت نشد.")
        return

    sem = asyncio.Semaphore(args.concurrency)
    tasks = [
        test_user_session(sem, uid, data, i + 1, total_users, args.delay, args.timeout)
        for i, (uid, data) in enumerate(users_map.items())
    ]

    print("🚀 شروع بررسی اتصال زنده اکانت‌ها در بله (دقیقاً ۱ بار به ازای هر اکانت)...")
    results = await asyncio.gather(*tasks)
    total_duration = time.time() - t_start

    alive_users = [r for r in results if r.get("status") == "alive"]
    dead_users = [r for r in results if r.get("status") != "alive"]

    print("\n" + "=" * 68)
    print(f"🏁 پایان اعتبارسنجی در {total_duration:.1f} ثانیه")
    print(f"✅ اکانت‌های سالم و فعال بدون تکرار (Unique Alive Users): {len(alive_users):,}")
    print(f"❌ اکانت‌های سوخته / منقضی: {len(dead_users):,}")
    print("=" * 68)

    # Save to JSON
    out_file = target_dir / args.output
    clean_alive = []
    for u in alive_users:
        clean_alive.append({
            "user_id": u["user_id"],
            "name": u["name"],
            "username": u["username"],
            "is_deleted_account": u["is_deleted"],
            "session_format": u["session_format"],
            "jwt": u["jwt"],
            "sources": u["sources"],
        })

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(clean_alive, f, ensure_ascii=False, indent=2)
    os.chmod(out_file, 0o600)
    print(f"💾 لیست اکانت‌های سالم (بدون تکرار) در فایل زیر ذخیره شد:\n   {out_file}")

    if args.export_sessions:
        export_dir = target_dir / "exported_sessions"
        export_dir.mkdir(parents=True, exist_ok=True)
        for u in clean_alive:
            sf = export_dir / f"{u['user_id']}.session"
            sf.write_text(u["session_format"], encoding="utf-8")
            os.chmod(sf, 0o600)
        print(f"📦 فایل‌های .session هر اکانت در پوشه زیر ذخیره شد:\n   {export_dir}")


if __name__ == "__main__":
    asyncio.run(main())
