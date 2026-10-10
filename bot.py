from telegram import Update
from telegram.ext import Application, CommandHandler,ContextTypes,MessageHandler,filters
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
async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text

    if message == "hello":
        await update.message.reply_text("Hello, friend! 👋")

    elif message == "hi":
        await update.message.reply_text("Hey there!")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start" , greet))
app.add_handler(CommandHandler("help" ,help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))
asyncio.set_event_loop(asyncio.new_event_loop())
app.run_polling()
