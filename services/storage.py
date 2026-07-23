import json
from pathlib import Path

SNAPSHOT_FILE = Path("data/snapshot.json")


def load_snapshot():
    if not SNAPSHOT_FILE.exists():
        return {}

    with open(SNAPSHOT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_snapshot(snapshot):
    SNAPSHOT_FILE.parent.mkdir(exist_ok=True)

    with open(SNAPSHOT_FILE, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=4, ensure_ascii=False)