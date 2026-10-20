import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Example ideas only; these are not verified live vacancies.
SAMPLE_JOBS = [
    "Python Developer Intern — check the employer's official careers page",
    "Cloud Support Associate — check the employer's official careers page",
    "Junior QA Tester — check the employer's official careers page",
    "Data Analyst Intern — check the employer's official careers page",
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.effective_message.reply_text(
        "👋 Welcome to Job Alert Bot!\nUse /jobs to see sample job-search ideas."
    )


async def jobs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "💼 Sample job-search ideas:\n\n" + "\n".join(
        f"• {item}" for item in SAMPLE_JOBS
    )
    message += "\n\nThese are examples, not confirmed current vacancies. Verify listings on official employer sites."
    await update.effective_message.reply_text(message)


def main():
    if not TOKEN:
        raise RuntimeError("Set TELEGRAM_BOT_TOKEN to a new token from BotFather.")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("jobs", jobs))
    logger.info("Job Alert Bot is starting.")
    app.run_polling()


if __name__ == "__main__":
    main()
