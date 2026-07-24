from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = "https://egy.voxcinemas.com"

CINEMA = {
    "name": "City Centre Almaza",
    "slug": "city-centre-almaza"
}

SHOWTIMES_URL = (
    f"{BASE_URL}/showtimes?c={CINEMA['slug']}"
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )
}

SHOWTIMES_URL = "https://egy.voxcinemas.com/showtimes?c=city-centre-almaza"

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")