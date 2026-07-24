import requests

from config import DISCORD_WEBHOOK


MAX_LENGTH = 1900


def send_notification(changes):

    if not changes:
        return

    header = "🎬 **VOX Booking Update**\n\n"

    current = header

    for change in changes:

        if len(current) + len(change) + 1 > MAX_LENGTH:

            requests.post(
                DISCORD_WEBHOOK,
                json={"content": current},
                timeout=30,
            )

            current = header

        current += change + "\n"

    if current != header:

        requests.post(
            DISCORD_WEBHOOK,
            json={"content": current},
            timeout=30,
        )