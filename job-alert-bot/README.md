# Telegram Job Alert Bot

A small Python Telegram bot that shares sample job-search ideas through the `/jobs` command.

## Commands
- `/start` — welcome and instructions
- `/jobs` — show example job-search ideas

**Important:** The sample entries are not verified live vacancies. This starter does not scrape job boards or send automated alerts from live sources.

## Run locally (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:TELEGRAM_BOT_TOKEN = "YOUR_NEW_TELEGRAM_BOT_TOKEN"
python bot.py
```

Never commit a real bot token, `.env` file, or other credentials.
