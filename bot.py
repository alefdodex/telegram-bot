from telegram.ext import ApplicationBuilder, CommandHandler
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("Bot sudah aktif!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # REGISTER COMMANDS YANG VALID
    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == "__main__":
    main()
