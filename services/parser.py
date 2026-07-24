from bs4 import BeautifulSoup


BLACKLIST = {
    "About",
    "Help & Support",
    "Explore Our Site",
    "Download our mobile app",
    "Stay in touch",
}


def get_movies(html: str):

    soup = BeautifulSoup(html, "html.parser")

    movies = []

    for h2 in soup.find_all("h2"):

        title = h2.get_text(strip=True)

        if title in BLACKLIST:
            continue

        movies.append(title)

    return movies