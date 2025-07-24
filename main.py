import telebot
import os
from dotenv import load_dotenv
load_dotenv()
import pprint


API_KEY = os.getenv('telegram_bot_token')
bot = telebot.TeleBot(API_KEY) 

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    pprint.pprint(message.__dict__, width=4)


bot.infinity_polling()