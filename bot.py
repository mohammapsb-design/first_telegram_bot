from telegram import Update
from telegram.ext import Application, CommandHandler,ContextTypes
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is missing. Check your .env file.")
async def greet(update : Update,context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hi friend!")
async def help_command(update : Update,context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I can't help you")
app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start" , greet))
app.add_handler(CommandHandler("help" ,help_command))
asyncio.set_event_loop(asyncio.new_event_loop())
app.run_polling()
