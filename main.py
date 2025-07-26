import telebot
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
load_dotenv()
import pprint


API_KEY = os.getenv('telegram_bot_token')
bot = telebot.TeleBot(API_KEY) 


# # message handler is a trigger base decorator you can modify it they are four ways to do that:
# # regex, command, content_type, chat_type(i dont know the meaning), func(i dont know this too)
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, "hello friend whats up with life?")


# @bot.message_handler(content_types=['document'])
# def react_to_audio(message):
#     bot.send_message(message.chat.id, "oh you sent me a document, are you horse?")


# @bot.message_handler(regexp="hello")
# def react_to_audio(message):
#     bot.send_message(message.chat.id, "hello mother fucker")


# #in lambda format if the result of the lambda is True function will be triggered
# # @bot.message_handler(func= lambda message: message.chat.username == 'cinaze')
# # def react_to_cina(message):
# #     bot.send_message(message.chat.id, "hello cina ")


# #you can write the function like a normal function too
# def normal_function(message):
#     return message.chat.username == 'cinaze'


# @bot.message_handler(func=normal_function)
# def react_to_cina(message):
#     bot.send_message(message.chat.id, "hello cina ")


# @bot.edited_message_handler(func=lambda message: True)
# def edited_message(message):
#     bot.send_message(message.chat.id, "oh you edited your message mother fucker")

# # if you write two of the message_handler decorator in one line in one paranteses it will get 'and' format
# # if you write two decorators for one function it will get 'or' format
# # if two functions conditions were true the function which came first it will be called 

#now we want to set a sequence of happenings to get some data from user
#there somthing called register_next_step_handler in the documentation
# @bot.message_handler(commands=['setInfo'])
# def set_info(message):
#     bot.send_message(message.chat.id, "what is your name?")
#     bot.register_next_step_handler(message, get_name)


# def get_name(message):
#     name = message.text
#     bot.send_message(message.chat.id, f'what is your last name?')
#     bot.register_next_step_handler(message, get_last_name, name)


# def get_last_name(message, name):
#     last_name = message.text
#     bot.send_message(message.chat.id, f'welcome {name} {last_name} to our tiny little world')

#lets talk about buttons 
#all of the buttons you define in your code will be in an object and then it will be sent to client
@bot.message_handler(commands=['start'])
def using_bottom(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('hi'))
    markup.add('hello')

    bot.send_message(message.chat.id, 'hello welcome to our comunity', reply_markup=markup)


bot.infinity_polling()