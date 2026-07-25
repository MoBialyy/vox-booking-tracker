import json
from services.snapshot import build_snapshot
from services.storage import save_snapshot
from services.storage import load_snapshot
from services.comparer import compare_snapshots
from services.discord import send_notification
from services.telegram import send_notification as send_telegram
from services.telegram_updates import check_updates

def main():

    try:
        check_updates()
    except Exception as e:
        print(f"Telegram update error: {e}")
    old_snapshot = load_snapshot()

    new_snapshot = build_snapshot()

    changes = compare_snapshots(old_snapshot, new_snapshot)

    if changes:

        print("Changes detected:")

        for change in changes:
            print(change)

        send_notification(changes)      # Discord
        send_telegram(changes)          # Telegram

    else:

        print("No changes detected.")

    save_snapshot(new_snapshot)


if __name__ == "__main__":
    main()