from telegram.ext import ApplicationBuilder, CommandHandler
from config import TELEGRAM_BOT_TOKEN

async def start(update, context):
    await update.message.reply_text("Bot sudah aktif, bro!")

async def echo(update, context):
    await update.message.reply_text(update.message.text)

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("", echo))

    app.run_polling()

if __name__ == "__main__":
    main()
