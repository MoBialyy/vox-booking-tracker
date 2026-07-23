import logging
from playwright.sync_api import sync_playwright
from config import SHOWTIMES_URL

logger = logging.getLogger(__name__)


def fetch_page():
    logger.info("Launching Chromium...")

    playwright = sync_playwright().start()

    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page()

    logger.info("Opening VOX...")

    page.goto(
        SHOWTIMES_URL,
        wait_until="domcontentloaded"
    )

    page.wait_for_timeout(5000)

    logger.info("Page loaded.")

    return page, browser, playwright