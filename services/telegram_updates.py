import json
from pathlib import Path

import requests

from config import TELEGRAM_API
from services.telegram_users import add_user, remove_user, load_users

OFFSET_FILE = Path("data/telegram_offset.json")

def load_offset():

    if not OFFSET_FILE.exists():
        return 0

    with open(OFFSET_FILE, "r", encoding="utf-8") as f:
        return json.load(f)["offset"]

def save_offset(offset):

    with open(OFFSET_FILE, "w", encoding="utf-8") as f:
        json.dump({"offset": offset}, f, indent=4)

def handle_update(update):

    message = update.get("message")

    if not message:
        return

    text = message.get("text", "")

    chat = message["chat"]

    chat_id = chat["id"]
    username = chat.get("username")
    first_name = chat.get("first_name")

    if text == "/start":

        add_user(
            chat_id=chat_id,
            username=username,
            first_name=first_name,
        )

        requests.post(
            f"{TELEGRAM_API}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": (
                    "🎬 Welcome to VOX Booking Tracker!\n\n"
                    "You are now subscribed.\n\n"
                    "Available commands:\n\n"
                    "▶️ /start - Subscribe to notifications\n"
                    "⏹️ /stop - Unsubscribe from notifications\n"
                    "📊 /status - Show your subscription status\n"
                    "❓ /help - Show this message"
                ),
            },
            timeout=30,
        )
    elif text == "/stop":

        remove_user(chat_id)

        requests.post(
            f"{TELEGRAM_API}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": (
                    "👋 You have been unsubscribed.\n\n"
                    "Send /start anytime to subscribe again."
                ),
            },
            timeout=30,
        )
    elif text == "/status":

        users = load_users()

        subscribed = any(
            user["chat_id"] == chat_id
            for user in users
        )

        status = "✅ Active" if subscribed else "❌ Not subscribed"

        requests.post(
            f"{TELEGRAM_API}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": (
                    "🎬 *VOX Booking Tracker*\n\n"
                    "📍 Cinema: City Centre Almaza\n"
                    "📅 Watching: Next 10-14 days\n\n"
                    f"Subscription: {status}"
                ),
                "parse_mode": "Markdown",
            },
            timeout=30,
        )
    elif text == "/help":

        requests.post(
            f"{TELEGRAM_API}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": (
                    "🤖 *VOX Booking Tracker*\n\n"
                    "Available commands:\n\n"
                    "▶️ /start - Subscribe to notifications\n"
                    "⏹️ /stop - Unsubscribe from notifications\n"
                    "📊 /status - Show your subscription status\n"
                    "❓ /help - Show this message"
                ),
                "parse_mode": "Markdown",
            },
            timeout=30,
        )
    

def check_updates():

    offset = load_offset()

    response = requests.get(
        f"{TELEGRAM_API}/getUpdates",
        params={
            "offset": offset,
            "timeout": 0,
        },
        timeout=30,
    )

    response.raise_for_status()

    updates = response.json()["result"]

    highest_offset = offset

    for update in updates:

        handle_update(update)

        highest_offset = max(
            highest_offset,
            update["update_id"] + 1,
        )

    save_offset(highest_offset)

