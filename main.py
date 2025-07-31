import telebot
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
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
# @bot.message_handler(commands=['start'])
# def using_bottom(message):
#     markup = ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.add(KeyboardButton('hi'))
#     markup.add('hello')

#     bot.send_message(message.chat.id, 'hello welcome to our comunity', reply_markup=markup)

#inline keyboard 
# from telebot.util import quick_markup

# @bot.message_handler(regexp="hello")
# def inline_keyboard(message):
#     markup = InlineKeyboardMarkup()
#     three = InlineKeyboardButton(text='scenario three', callback_data='three')
#     two = InlineKeyboardButton(text='scenario two', callback_data='two') 
#     one = InlineKeyboardButton(text='scenario one', callback_data='one') 
#     markup.add(one)
#     markup.add(three)
#     markup.add(two)
#     bot.send_message(message.chat.id, 'hello welcome to our comunity', reply_markup=markup)


# @bot.callback_query_handler(func=lambda call: True)
# def call_back_hanler(call):
#     pprint.pprint(call.data, width=4)
#     pprint.pprint(call.__dict__)
#     if call.data == 'one':
#         bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
#         markup = InlineKeyboardMarkup()
#         exit = InlineKeyboardButton(text='exit', callback_data='exit')
#         five = InlineKeyboardButton(text='scenario five', callback_data='five') 
#         six = InlineKeyboardButton(text='scenario six', callback_data='six') 
#         markup.add(six)
#         markup.add(exit)
#         markup.add(five)
#         bot.send_message(call.message.chat.id, 'this is second scenario', reply_markup=markup)
#     if call.data == 'two':
#         bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
#         markup = InlineKeyboardMarkup()
#         seven = InlineKeyboardButton(text='scenario seven', callback_data='seven')
#         eight = InlineKeyboardButton(text='scenario eight', callback_data='eight') 
#         nine = InlineKeyboardButton(text='scenario nine', callback_data='nine') 
#         markup.add(nine)
#         markup.add(seven)
#         markup.add(eight)
#         bot.send_message(call.message.chat.id, 'this is third scenario', reply_markup=markup)
#     if call.data == 'exit':
#         bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)

@bot.message_handler(commands=['test_files'])
def sending_files_handler(message):
    
    markup = InlineKeyboardMarkup()
    voice = InlineKeyboardButton(text='voice', callback_data='voice')
    video = InlineKeyboardButton(text='video', callback_data='video')
    document = InlineKeyboardButton(text='document', callback_data='document')
    markup.add(voice)
    markup.add(video)
    markup.add(document)
    bot.send_message(message.chat.id, 'which file option do you want?', reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call: call.message.text == 'which file option do you want?')
def file_callback_handler(call):
    if call.data == "voice":
        pprint.pprint(call.__dict__)
        voice = open('./test_files/file_example_MP3_1MG.mp3', 'rb')
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_chat_action(chat_id=call.message.chat.id, action="upload_voice")
        bot.send_audio(chat_id=call.message.chat.id , audio=voice)
    if call.data == "video":
        video = open('./test_files/file_example_MP4_480_1_5MG.mp4', 'rb')
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

        bot.send_video(chat_id=call.message.chat.id, video=video)
    if call.data == "document":
        doc = open('./test_files/file-sample_100kB.doc', 'rb') 
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_document(chat_id=call.message.chat.id, document=doc)


bot.infinity_polling()