from datetime import datetime


def get_movies(page):
    """
    Returns all movie titles visible on the current page.
    """

    movies = []

    for title in page.locator("article.movie-compare h2").all():

        name = title.inner_text().strip()

        if name:
            movies.append(name)

    return movies


def get_date_urls(page):
    """
    Returns:
    [
        ("2026-07-24", "https://..."),
        ("2026-07-25", "https://..."),
        ...
    ]
    """

    results = []

    for link in page.locator("a").all():

        try:
            text = link.inner_text().strip()
            href = link.get_attribute("href")

            if not href:
                continue

            if "/showtimes?" not in href:
                continue

            if "&d=" not in href:
                continue

            raw_date = href.split("&d=")[1]

            iso_date = datetime.strptime(
                raw_date,
                "%Y%m%d"
            ).strftime("%Y-%m-%d")

            full_url = "https://egy.voxcinemas.com" + href

            results.append((iso_date, full_url))

        except Exception:
            pass

    return results