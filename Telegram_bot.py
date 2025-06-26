import os
import telebot
from dotenv import load_dotenv
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'body.settings')
django.setup()

from core.models import TelegramPico

# Load bot token
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    username = message.from_user.username
    if username:
        obj, created = TelegramPico.objects.get_or_create(username=username)
        if created:
            bot.send_message(message.chat.id, f"Hi @{username}, you've been registered! ✅")
        else:
            bot.send_message(message.chat.id, f"Welcome back @{username}, you're already registered.")
    else:
        bot.send_message(message.chat.id, "You need a Telegram username to register ❗")

def start_bot():
    print("Bot is polling...")
    bot.polling()

if __name__ == "__main__":
    start_bot()
