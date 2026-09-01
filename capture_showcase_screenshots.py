#!/usr/bin/env python3
"""Capture homepage screenshots for the AI design showcase."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "ai-showcase-sites.json"
OUT = ROOT / "ai-showcase-screenshots"
VIEWPORT = {"width": 1280, "height": 800}


def main() -> int:
    payload = json.loads(DATA.read_text())
    sites = payload["sites"]
    OUT.mkdir(parents=True, exist_ok=True)

    ok, failed = 0, []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport=VIEWPORT,
            device_scale_factor=1,
            user_agent=(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            ),
        )
        page = context.new_page()

        for i, site in enumerate(sites, 1):
            slug = site["slug"]
            url = site["url"]
            out_path = OUT / f"{slug}.jpg"
            print(f"[{i:02d}/{len(sites)}] {site['name']} -> {out_path.name}")

            try:
                page.goto(url, wait_until="domcontentloaded", timeout=45000)
                page.wait_for_timeout(2500)
                page.screenshot(
                    path=str(out_path),
                    full_page=False,
                    type="jpeg",
                    quality=82,
                    clip={"x": 0, "y": 0, "width": 1280, "height": 800},
                    timeout=60000,
                    animations="disabled",
                )
                ok += 1
            except Exception as exc:  # noqa: BLE001
                failed.append((slug, str(exc)))
                print(f"  FAILED: {exc}", file=sys.stderr)

        browser.close()

    print(f"\nDone: {ok} captured, {len(failed)} failed")
    for slug, err in failed:
        print(f"  - {slug}: {err}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
