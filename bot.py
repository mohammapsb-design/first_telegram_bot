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
    user = update.message.from_user
    name = user.first_name
    if message == "hello":
        await update.message.reply_text(f"Hello, {name}! 👋")

    elif message == "hi":
        await update.message.reply_text("Hey there!")
    if message == "me":
        await update.message.reply_text(f'''
ID : {user.id}
Username : {user.username}
Firstname : {user.first_name}
''')
app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start" , greet))
app.add_handler(CommandHandler("help" ,help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))
asyncio.set_event_loop(asyncio.new_event_loop())
app.run_polling()
