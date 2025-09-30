from telegram.ext import Application, CommandHandler
import os

TOKEN = os.getenv("8462737921:AAGN7uxkA4VpOuyHrMYreq07Fc95_uuR8g4
")

async def start(update, context):
    await update.message.reply_text("Hello! Your Gym Coach bot is alive 🚀")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

