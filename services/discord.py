import requests

from config import DISCORD_WEBHOOK


def send_notification(changes):

    if not changes:
        return

    message = "\n".join(changes)

    requests.post(
        DISCORD_WEBHOOK,
        json={
            "content": f"🎬 **VOX Booking Update**\n\n{message}"
        },
        timeout=30,
    )