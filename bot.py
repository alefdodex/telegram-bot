from telegram.ext import ApplicationBuilder, CommandHandler
import config

async def start(update, context):
    await update.message.reply_text("Bot sudah aktif!")

def main():
    app = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    # REGISTER COMMAND /start
    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == "__main__":
    main()
