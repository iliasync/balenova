"""Record outbound traffic produced by the official Bale web application."""

from __future__ import annotations

import argparse
import asyncio
import shutil
from collections.abc import Coroutine
from pathlib import Path
from typing import Any

from bale import ProtocolRecorder
from bale.research import OfficialWebCapture


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default="https://web.bale.ai")
    parser.add_argument(
        "--profile",
        default="protocol/browser-profile",
        help="Persistent Chromium profile (contains the web login)",
    )
    parser.add_argument(
        "--show-secrets",
        action="store_true",
        help="DANGEROUS: include authentication frames and secret fields",
    )
    parser.add_argument(
        "--watch",
        type=float,
        help="Stop automatically after this many seconds (default: until Ctrl+C)",
    )
    parser.add_argument(
        "--headless", action="store_true", help="Run without a visible browser window"
    )
    parser.add_argument(
        "--executable-path",
        default=shutil.which("google-chrome") or shutil.which("chromium"),
        help="Chrome/Chromium executable; defaults to a system browser when found",
    )
    return parser.parse_args()


async def main() -> None:
    args = parse_args()
    try:
        from playwright.async_api import async_playwright
    except ImportError as error:
        raise SystemExit(
            "Install research tools first:\n"
            "  pip install -e '.[research]'\n"
            "  playwright install chromium"
        ) from error

    recorder = ProtocolRecorder("protocol/traces", include_secrets=args.show_secrets)
    await recorder.start()
    capture = OfficialWebCapture(recorder)
    tasks: set[asyncio.Task[None]] = set()

    def schedule(coroutine: Coroutine[Any, Any, None]) -> None:
        task = asyncio.create_task(coroutine)
        tasks.add(task)
        task.add_done_callback(tasks.discard)

    async def capture_request(request: Any) -> None:
        headers = await request.all_headers()
        if "grpc-web" not in headers.get("content-type", "").casefold():
            return
        body = request.post_data_buffer
        if body:
            await capture.grpc_frame("outbound", body, url=request.url)

    async def capture_response(response: Any) -> None:
        headers = await response.all_headers()
        if "grpc-web" not in headers.get("content-type", "").casefold():
            return
        try:
            body = await response.body()
        except Exception as error:
            await recorder.record(
                transport="official-web-grpc",
                direction="inbound",
                kind="official_grpc_capture_error",
                error=str(error),
                details={"url": response.url},
            )
            return
        await capture.grpc_frame("inbound", body, url=response.url)

    def attach_page(page: Any) -> None:
        page.on("request", lambda request: schedule(capture_request(request)))
        page.on("response", lambda response: schedule(capture_response(response)))

        def attach_websocket(websocket: Any) -> None:
            websocket.on(
                "framesent",
                lambda payload: schedule(
                    capture.websocket_frame("outbound", payload, url=websocket.url)
                ),
            )
            websocket.on(
                "framereceived",
                lambda payload: schedule(
                    capture.websocket_frame("inbound", payload, url=websocket.url)
                ),
            )

        page.on("websocket", attach_websocket)

    print("A persistent Chromium window will open with the official Bale web app.")
    print("Log in once, then click buttons or start the feature being studied.")
    print("Press Ctrl+C here when finished. Do not publish the resulting trace.")

    async with async_playwright() as playwright:
        launch_options = {
            "user_data_dir": Path(args.profile),
            "headless": args.headless,
        }
        if args.executable_path:
            launch_options["executable_path"] = args.executable_path
        context = await playwright.chromium.launch_persistent_context(**launch_options)
        context.on("page", attach_page)
        for page in context.pages:
            attach_page(page)
        page = context.pages[0] if context.pages else await context.new_page()
        await page.goto(args.url, wait_until="domcontentloaded", timeout=60_000)
        try:
            if args.watch is None:
                await asyncio.Event().wait()
            elif args.watch > 0:
                await asyncio.sleep(args.watch)
        except asyncio.CancelledError:
            print("\nStopping official web capture...")
        finally:
            await context.close()

    if tasks:
        await asyncio.gather(*tuple(tasks), return_exceptions=True)
    print(f"Trace saved to: {recorder.path}")
    print(f"Report: python -m bale.tools.proto report {recorder.path}")


if __name__ == "__main__":
    asyncio.run(main())
