from curl_cffi import requests


def fetch_html(url: str) -> str:

    response = requests.get(
        url,
        impersonate="chrome",
        timeout=30,
    )

    response.raise_for_status()

    return response.text