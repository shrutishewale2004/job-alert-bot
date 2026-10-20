# Telegram Weather Bot

A Python Telegram bot that retrieves current temperature and conditions for a city using the OpenWeather API.

## Commands
- `/start` — display instructions
- `/weather <city>` — retrieve current weather

## Run locally (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
$env:TELEGRAM_BOT_TOKEN = "YOUR_NEW_TELEGRAM_BOT_TOKEN"
$env:OPENWEATHER_API_KEY = "YOUR_NEW_OPENWEATHER_API_KEY"
python bot.py
```

Use newly generated credentials. Never commit real tokens or API keys.
