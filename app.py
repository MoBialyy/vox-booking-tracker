import json
from services.snapshot import build_snapshot
from services.storage import save_snapshot
from services.storage import load_snapshot
from services.comparer import compare_snapshots
from services.discord import send_notification

def main():

    old_snapshot = load_snapshot()

    new_snapshot = build_snapshot()

    changes = compare_snapshots(old_snapshot, new_snapshot)

    if changes:

        print("Changes detected:")

        for change in changes:
            print(change)

        send_notification(changes)

    else:

        print("No changes detected.")

    save_snapshot(new_snapshot)


if __name__ == "__main__":
    main()