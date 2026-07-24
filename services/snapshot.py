from collections import Counter
from datetime import datetime, timedelta

from config import SHOWTIMES_URL
from services.fetcher import fetch_html
from services.parser import get_movies

LOOKAHEAD_DAYS = 14


def build_snapshot():

    snapshot = {}

    consecutive_empty = 0

    for i in range(LOOKAHEAD_DAYS):

        date = datetime.today() + timedelta(days=i)

        display_date = date.strftime("%Y-%m-%d")
        vox_date = date.strftime("%Y%m%d")

        url = f"{SHOWTIMES_URL}&d={vox_date}"

        print(f"Scanning {display_date}")

        try:

            html = fetch_html(url)

            movies = get_movies(html)

            if not movies:

                consecutive_empty += 1

                print("Found 0 movies")

                if consecutive_empty >= 3:
                    break

                continue

            consecutive_empty = 0

            snapshot[display_date] = dict(Counter(movies))

            print(f"Found {len(movies)} movies")

        except Exception as e:

            print(e)

    return snapshot