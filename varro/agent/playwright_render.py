import asyncio
from playwright.async_api import async_playwright, Browser
from playwright.async_api import Error

__all__ = ["start_browser", "stop_browser", "html_to_png"]

# Global singletons
_playwright = None  # type: ignore
_browser: Browser | None = None
_lock = asyncio.Lock()

# Chrome flags that silence GPU/UPower warnings & improve stability in containers
CHROME_FLAGS = [
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu-sandbox",
    "--use-gl=swiftshader",
    # "--disable-software-rasterizer",
    "--ignore-gpu-blocklist",
    "--enable-webgl",
    "--enable-accelerated-2d-canvas",
    "--disable-features=VizDisplayCompositor",
    "--hide-scrollbars",
    "--mute-audio",
    "--disable-features=BatteryMonitor",
]


async def start_browser() -> None:
    """
    Launch headless Chromium once and keep it for reuse.
    Call this from the app's startup event so the cost is paid up‑front.
    """
    global _playwright, _browser
    async with _lock:
        if _browser is None:
            _playwright = await async_playwright().start()
            _browser = await _playwright.chromium.launch(
                headless=True,
                args=CHROME_FLAGS,
            )
            # Optional warm‑up (makes the very first screenshot faster)
            page = await _browser.new_page()
            await page.close()


async def stop_browser() -> None:
    """Cleanly close Chromium & Playwright (call from shutdown event)."""
    global _playwright, _browser
    async with _lock:
        if _browser:
            await _browser.close()
            _browser = None
        if _playwright:
            await _playwright.stop()
            _playwright = None


async def html_to_png(html: str, *, width: int = 600, height: int = 400) -> bytes:
    """
    Render a Plotly HTML string to PNG bytes.
    - Waits until Plotly's graph SVG/canvas is present
    """
    if _browser is None:  # safety net (should be started already)
        await start_browser()

    page = await _browser.new_page(  # type: ignore[arg-type]
        viewport={"width": width, "height": height}
    )

    try:
        # Just load the HTML
        await page.set_content(html)

        # Wait until the Plotly graph actually rendered something:
        # either an SVG with class .main-svg or a canvas inside the plot container.
        await page.wait_for_selector(
            ".plotly-graph-div .main-svg, .plotly-graph-div canvas",
            timeout=10_000,  # ms
            state="visible",
        )

        # Optional tiny extra delay if you ever see partial renders:
        # await page.wait_for_timeout(100)

        png_bytes = await page.screenshot(type="png")
        return png_bytes
    finally:
        await page.close()
