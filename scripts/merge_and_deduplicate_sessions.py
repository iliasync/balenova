#!/usr/bin/env python3
"""
Merge and Deduplicate Valid Bale Sessions
=========================================
Takes valid session JSON files from multiple sources, deduplicates strictly by user_id,
combines their source archives, and creates a clean consolidated directory containing:
  1. Individual {user_id}.session files (with 0600 permissions)
  2. A detailed descriptive metadata JSON file (all_valid_users.json)
  3. A Markdown summary report (README.md)

Usage:
    .venv/bin/python scripts/merge_and_deduplicate_sessions.py
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent


def main():
    parser = argparse.ArgumentParser(description="تجمیع و حذف تکراری‌های سشن‌های سالم بر اساس User ID")
    parser.add_argument(
        "--inputs",
        nargs="+",
        default=[
            "/home/mahan/Downloads/Telegram Desktop/sessions/valid_unique_users.json",
            "/home/mahan/Downloads/ses/valid_unique_users.json",
        ],
        help="مسیر فایل‌های JSON حاوی سشن‌های سالم",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default="/home/mahan/Downloads/all_valid_sessions",
        help="پوشه خروجی نهایی برای سشن‌های یکتا",
    )
    args = parser.parse_args()

    out_dir = Path(args.output_dir).expanduser().resolve()
    sessions_dir = out_dir / "sessions"
    out_dir.mkdir(parents=True, exist_ok=True)
    sessions_dir.mkdir(parents=True, exist_ok=True)

    merged_users: dict[int, dict] = {}
    sources_stats: dict[str, int] = {}

    print("=" * 68)
    print("🔄 در حال تجمیع و حذف تکراری سشن‌های سالم بر اساس User ID...")
    print("=" * 68)

    for in_path_str in args.inputs:
        in_path = Path(in_path_str).expanduser().resolve()
        if not in_path.exists():
            print(f"⚠️  فایل ورودی پیدا نشد: {in_path}", file=sys.stderr)
            continue

        with open(in_path, encoding="utf-8") as f:
            data = json.load(f)

        sources_stats[in_path.name] = len(data)
        print(f"📄 فایل {in_path.name}: شامل {len(data):,} کاربر سالم")

        for item in data:
            uid = item["user_id"]
            if uid not in merged_users:
                merged_users[uid] = {
                    "user_id": uid,
                    "name": item.get("name") or "",
                    "username": item.get("username") or "",
                    "is_deleted_account": item.get("is_deleted_account", False),
                    "session_format": item.get("session_format"),
                    "jwt": item.get("jwt"),
                    "sources": set(item.get("sources", [])),
                }
            else:
                # Merge sources
                merged_users[uid]["sources"].update(item.get("sources", []))
                # If existing name was empty or deleted, update if this one has a proper name
                if not merged_users[uid]["name"] and item.get("name"):
                    merged_users[uid]["name"] = item.get("name")
                if not merged_users[uid]["username"] and item.get("username"):
                    merged_users[uid]["username"] = item.get("username")

    total_unique = len(merged_users)
    active_named = [u for u in merged_users.values() if not u["is_deleted_account"]]
    deleted_accounts = [u for u in merged_users.values() if u["is_deleted_account"]]

    print("-" * 68)
    print(f"🎯 مجموع کل اکانت‌های سالم و یکتا (بدون هیچ تکراری): {total_unique:,}")
    print(f"   👤 اکانت‌های نام‌دار و فعال: {len(active_named):,}")
    print(f"   🗑️  اکانت‌های دیلیت‌شده (Deleted Account): {len(deleted_accounts):,}")
    print("-" * 68)

    # Export individual .session files
    exported_count = 0
    for uid, u in merged_users.items():
        session_file = sessions_dir / f"{uid}.session"
        session_file.write_text(u["session_format"], encoding="utf-8")
        os.chmod(session_file, 0o600)
        exported_count += 1

    # Prepare JSON description
    final_users_list = []
    # Sort: active accounts first, then deleted
    sorted_users = sorted(
        merged_users.values(),
        key=lambda x: (x["is_deleted_account"], str(x["name"]).casefold()),
    )

    for i, u in enumerate(sorted_users, 1):
        final_users_list.append({
            "index": i,
            "user_id": u["user_id"],
            "name": u["name"] or "Deleted Account",
            "username": u["username"] or "",
            "status": "deleted_account" if u["is_deleted_account"] else "active",
            "session_file": f"sessions/{u['user_id']}.session",
            "session_format": u["session_format"],
            "jwt": u["jwt"],
            "found_in_sources": sorted(list(u["sources"])),
        })

    json_out = out_dir / "all_valid_users.json"
    with open(json_out, "w", encoding="utf-8") as f:
        json.dump(
            {
                "generated_at": datetime.now().isoformat(),
                "total_unique_users": total_unique,
                "active_accounts_count": len(active_named),
                "deleted_accounts_count": len(deleted_accounts),
                "users": final_users_list,
            },
            f,
            ensure_ascii=False,
            indent=2,
        )
    os.chmod(json_out, 0o600)

    # Write a comprehensive Markdown README
    readme_path = out_dir / "README.md"
    readme_content = f"""# آرشیو نهایی سشن‌های سالم بله (کاملاً یکتا و بدون تکرار)

* **تاریخ ساخت:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
* **کل اکانت‌های سالم و فعال:** **{total_unique}** اکانت منحصر‌به‌فرد
* **اکانت‌های دارای نام و پروفایل فعال:** {len(active_named)} عدد
* **اکانت‌های وضعیت Deleted Account:** {len(deleted_accounts)} عدد
* **پوشه سشن‌ها:** `sessions/` (شامل فایل‌های `.session` با نام شناسه هر کاربر)

---

## لیست اکانت‌های فعال و دارای نام ({len(active_named)} اکانت)

| # | شناسه کاربر (User ID) | نام اکانت | نام کاربری (Username) | فایل سشن |
| :-: | :-: | :-: | :-: | :-: |
"""
    idx = 1
    for u in sorted_users:
        if not u["is_deleted_account"]:
            uname = f"@{u['username']}" if u["username"] else "-"
            name = u["name"] or "-"
            readme_content += f"| {idx} | `{u['user_id']}` | {name} | {uname} | `sessions/{u['user_id']}.session` |\n"
            idx += 1

    readme_content += f"""
---

## لیست اکانت‌های دیلیت‌شده اما دارای سشن معتبر ({len(deleted_accounts)} اکانت)

| # | شناسه کاربر (User ID) | وضعیت | فایل سشن |
| :-: | :-: | :-: | :-: |
"""
    del_idx = 1
    for u in sorted_users:
        if u["is_deleted_account"]:
            readme_content += f"| {del_idx} | `{u['user_id']}` | Deleted Account | `sessions/{u['user_id']}.session` |\n"
            del_idx += 1

    readme_path.write_text(readme_content, encoding="utf-8")

    # Also make a copy in project's .private/ directory
    private_dir = PROJECT_ROOT / ".private" / "all_valid_sessions"
    private_dir.mkdir(parents=True, exist_ok=True)
    import shutil
    shutil.copy2(json_out, private_dir / "all_valid_users.json")
    shutil.copy2(readme_path, private_dir / "README.md")

    print("\n" + "=" * 68)
    print("✅ فرایند با موفقیت به پایان رسید!")
    print(f"📁 پوشه خروجی نهایی:\n   {out_dir}")
    print(f"📦 فایل‌های .session انفرادی ({exported_count} عدد):\n   {sessions_dir}")
    print(f"📊 فایل جیسون توضیحات جامع:\n   {json_out}")
    print(f"📄 گزارش مارک‌داون:\n   {readme_path}")
    print("=" * 68)


if __name__ == "__main__":
    main()
