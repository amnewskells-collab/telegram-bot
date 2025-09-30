import os
import logging
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
log = logging.getLogger("gym-coach-bot")

TOKEN = os.getenv("8462737921:AAGN7uxkA4Vp0uyHrMYreq07Fc95_uuR8g4")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Your Gym Coach bot is alive 🚀")

def main():
    if not TOKEN:
        log.error("TELEGRAM_TOKEN is missing!")
        raise SystemExit(1)

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    log.info("Bot is running…")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
