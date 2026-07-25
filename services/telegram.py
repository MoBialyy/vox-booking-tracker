import requests

from config import TELEGRAM_API
from services.telegram_users import load_users


def send_notification(changes):

    if not changes:
        return

    users = load_users()

    if not users:
        return

    message = "🎬 *VOX Booking Update*\n\n" + "\n".join(changes)

    for user in users:

        response = requests.post(
            f"{TELEGRAM_API}/sendMessage",
            json={
                "chat_id": user["chat_id"],
                "text": message,
                "parse_mode": "Markdown",
            },
            timeout=30,
        )

        response.raise_for_status()