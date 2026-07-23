from collections import Counter
from datetime import datetime, timedelta
from playwright.sync_api import sync_playwright

from config import SHOWTIMES_URL
from services.parser import get_movies


LOOKAHEAD_DAYS = 14


def build_snapshot():

    snapshot = {}

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        consecutive_empty = 0

        for i in range(LOOKAHEAD_DAYS):

            date = datetime.today() + timedelta(days=i)

            display_date = date.strftime("%Y-%m-%d")
            vox_date = date.strftime("%Y%m%d")

            url = f"{SHOWTIMES_URL}&d={vox_date}"

            print(f"Scanning {display_date}")

            page = browser.new_page()

            try:

                page.goto(
                    url,
                    wait_until="domcontentloaded",
                    timeout=30000
                )

                page.wait_for_timeout(3000)

                movies = get_movies(page)

                page.close()

                if not movies:
                    consecutive_empty += 1

                    if consecutive_empty >= 3:
                        break

                    continue

                consecutive_empty = 0

                snapshot[display_date] = dict(Counter(movies))

                print(f"  Found {len(movies)} movies")

            except Exception as e:

                print(e)

                page.close()

        browser.close()

    return snapshot