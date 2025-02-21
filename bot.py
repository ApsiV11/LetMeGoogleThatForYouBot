from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
)
import os
import logging

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        'Hello! Send me a message starting with "google" and I will generate a search link for you.'
    )


async def google_search(update: Update, context: CallbackContext) -> None:
    message = update.message.text.strip()
    if message.lower().startswith("google"):
        query = message[6:].strip()
        if query:
            search_url = f"https://letmegooglethat.com/?q={query.replace(' ', '+')}"
            await update.message.reply_text(f"Here you go: {search_url}")
        else:
            await update.message.reply_text(
                "You need to provide something to search for!"
            )


def main() -> None:
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN is not set!")
        return

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, google_search))

    app.run_polling()


if __name__ == "__main__":
    main()
