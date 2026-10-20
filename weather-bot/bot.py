import logging
import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(
        "🌦️ Welcome to Weather Bot!\nUse /weather <city> to check current weather."
    )


async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.effective_message.reply_text("Usage: /weather <city>")
        return
    if not OPENWEATHER_API_KEY:
        await update.effective_message.reply_text("Weather service is not configured.")
        logger.error("OPENWEATHER_API_KEY is missing.")
        return

    city = " ".join(context.args)
    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"q": city, "appid": OPENWEATHER_API_KEY, "units": "metric"},
            timeout=10,
        )
        payload = response.json()
    except (requests.RequestException, ValueError) as exc:
        logger.warning("Weather API request failed: %s", exc)
        await update.effective_message.reply_text("Weather service unavailable. Please try again.")
        return

    if response.status_code != 200 or str(payload.get("cod")) != "200":
        await update.effective_message.reply_text("City not found or weather data unavailable.")
        return

    temp = payload["main"]["temp"]
    description = payload["weather"][0]["description"]
    await update.effective_message.reply_text(
        f"🌡️ Temperature: {temp}°C\n🌦️ Condition: {description}"
    )


def main():
    if not TELEGRAM_BOT_TOKEN:
        raise RuntimeError("Set TELEGRAM_BOT_TOKEN to a new token from BotFather.")
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("weather", weather))
    logger.info("Weather Bot is starting.")
    app.run_polling()


if __name__ == "__main__":
    main()
