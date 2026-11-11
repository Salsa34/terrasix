import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Bot terrasix online di Koyeb!")

app = ApplicationBuilder().token(os.getenv("9148532415:AAHXBuaz5kLAMnT7wtzAVG3Keoqvfzb61mg")).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
