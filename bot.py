from telegram import Update
from telegram.ext import Application, CommandHandler,ContextTypes
from dotenv import load_dotenv
import os
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
async def greet(update : Update,context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hi friend!")
async def help(update : Update,context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I can't help you")
app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start" , greet))
app.add_handler(CommandHandler("help" ,help))
app.run_polling()