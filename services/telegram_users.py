import json
from pathlib import Path

USERS_FILE = Path("data/telegram_users.json")


def load_users():

    if not USERS_FILE.exists():
        return []

    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_users(users):

    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)


def add_user(chat_id, username, first_name):

    users = load_users()

    for user in users:

        if user["chat_id"] == chat_id:
            return

    users.append(
        {
            "chat_id": chat_id,
            "username": username,
            "first_name": first_name,
        }
    )

    save_users(users)

def remove_user(chat_id):

    users = load_users()

    users = [
        user
        for user in users
        if user["chat_id"] != chat_id
    ]

    save_users(users)