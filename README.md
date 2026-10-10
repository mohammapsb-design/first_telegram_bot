# First Telegram Bot

My first Telegram bot, built with Python using the `python-telegram-bot` library.

## Features

- `/start` - Start the bot.
- `/help` - Display the help message.

## Requirements

- Python 3.14.6
- python-telegram-bot 21.6
- python-dotenv

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/mohammapsb-design/first_telegram_bot.git
   cd first_telegram_bot
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Create a `.env` file in the projec<img width="1376" height="768" alt="1008174151" src="https://github.com/user-attachments/assets/4dbb7518-7963-4f65-b106-fce8fb49630b" />
t directory and add your bot token:

   ```env
   BOT_TOKEN=your_bot_token_here
   ```

5. Run the bot:

   ```bash
   python bot.py
   ```

## Notes

- Keep your bot token private.
- Never commit your `.env` file to GitHub.

## Status

This is a beginner project created for learning Python and Telegram bot development.y

