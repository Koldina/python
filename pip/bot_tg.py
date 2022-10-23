#https://core.telegram.org/bots/samples
#https://github.com/python-telegram-bot/python-telegram-bot
#https://python-telegram-bot.org/
#pip install python-telegram-bot --pre
#$ python bot.py

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("YOUR TOKEN HERE").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()

