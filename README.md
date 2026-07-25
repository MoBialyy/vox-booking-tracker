# 🎬 VOX Booking Tracker

A Python bot that monitors the VOX Cinemas Egypt website for showtime changes and notifies subscribers through Discord and Telegram.

The project runs automatically on GitHub Actions, so it works 24/7 without requiring your computer to stay online.

---

## Features

- 🎬 Tracks movie showtimes for a selected VOX cinema
- 🔍 Detects newly added and removed movies
- 📩 Sends instant notifications to Discord
- 🤖 Supports Telegram subscriptions
- 👥 Multiple Telegram users can subscribe independently
- ☁️ Runs automatically on GitHub Actions
- 💾 Stores snapshots to avoid duplicate notifications

---

## How It Works

Every scheduled run:

1. Reads any new Telegram commands (`/start`, `/stop`, etc.)
2. Downloads the latest VOX showtimes
3. Extracts the available movies
4. Compares them with the previous snapshot
5. Sends notifications if changes are detected
6. Saves the updated snapshot

---

## Telegram Commands

| Command | Description |
|---------|-------------|
| `/start` | Subscribe to notifications |
| `/stop` | Unsubscribe |
| `/status` | Show subscription status |
| `/help` | Show available commands |

---

## Tech Stack

- Python 3.11
- Playwright
- BeautifulSoup
- Requests
- GitHub Actions
- Discord Webhooks
- Telegram Bot API

---

## Project Structure

```
.
├── app.py
├── config.py
├── data/
│   ├── snapshot.json
│   ├── telegram_users.json
│   └── telegram_offset.json
├── services/
│   ├── comparer.py
│   ├── discord.py
│   ├── parser.py
│   ├── snapshot.py
│   ├── storage.py
│   ├── telegram.py
│   ├── telegram_updates.py
│   └── telegram_users.py
└── .github/
    └── workflows/
```

---

## Configuration

Create a `.env` file:

```env
DISCORD_WEBHOOK=...
TELEGRAM_BOT_TOKEN=...
```

GitHub Actions requires the same values as repository secrets.

---

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

---

## Future Improvements

- Support multiple VOX cinemas
- Watch specific movies only
- Custom notification preferences
- Daily summary mode
- Admin commands
- Web dashboard

---

## License

MIT License.
