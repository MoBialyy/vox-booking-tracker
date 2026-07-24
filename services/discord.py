import requests
from config import DISCORD_WEBHOOK


def send_notification(changes):

    if not changes:
        return

    print("Webhook loaded:", DISCORD_WEBHOOK is not None)

    message = "\n".join(changes)

    response = requests.post(
        DISCORD_WEBHOOK,
        json={
            "content": f"🎬 **VOX Booking Update**\n\n{message}"
        },
        timeout=30,
    )

    print("Discord status:", response.status_code)
    print("Discord response:", response.text)