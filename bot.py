import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = "MASUKKAN_TOKEN_BOT_KAMU_DI_SINI"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update, context):
    await update.message.reply_text("Bot sudah aktif bang! 😊")

async def echo(update, context):
    text = update.message.text
    await update.message.reply_text(f"Kamu bilang: {text}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    app.run_polling()

if __name__ == "__main__":
    main()
