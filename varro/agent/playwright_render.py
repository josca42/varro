import asyncio
from playwright.async_api import async_playwright, Browser

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
    Render an arbitrary HTML string to PNG bytes using the global browser.
    """
    if _browser is None:  # safety net (should be started already)
        await start_browser()

    page = await _browser.new_page(  # type: ignore[arg-type]
        viewport={"width": width, "height": height}
    )
    # wait_until="networkidle" ⇒ Plotly JS fully loaded before screenshot

    await page.set_content(html, wait_until="networkidle")
    png_bytes = await page.screenshot(type="png")
    await page.close()
    return png_bytes


async def test_webgl():
    await start_browser()
    context = await _browser.new_context()
    page = await context.new_page()
    info = await page.evaluate("""
    () => {
    const gl = document.createElement('canvas').getContext('webgl');
    return gl ? gl.getParameter(gl.VERSION) : 'No WebGL';
    }
    """)
    print(info)
    await stop_browser()


if __name__ == "__main__":
    asyncio.run(test_webgl())
