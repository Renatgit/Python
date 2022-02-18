import telebot
from telebot import types
import sqlite3

name=""
surname=""
age=0
country=""

bot=telebot.TeleBot("5133298745:AAHHhkpGEujc4hfz7YEUkvpIxdiJzwea_u4", parse_mode=None)
@bot.message_handler(commands=["start"])
def send_message(message):
    bot.send_message(message.from_user.id, "Привет, я готов к работе!")

@bot.message_handler(func=lambda m: True)
def a(message):
    if message.text=="Привет":
        bot.send_message(message.from_user.id, "Привет")
    elif message.text=="Какие у тебя функции?":
        bot.send_message(message.ftom_user.id, "У меня много функций!")
    elif message.text=="reg":
        bot.send_message(message.from_user.id, "Давай познакомимся, как тебя зовут?")
        bot.register_next_step_handler(message, registr_name)
    else:
        bot.reply_to(message.from_user.id, "Я не понимаю тебя!")

def registr_name(message):
    global name
    name=message.text
    bot.send_message(message.from_user.id, "Какая у вас фамилия?")
    bot.register_next_step_handler(message, registr_surname)

def registr_surname(message):
    global surname
    surname=message.text
    bot.send_message(message.from_user.id, "Сколько вам лет?")
    bot.register_next_step_handler(message, registr_age)

def registr_age(message):
    global age
    age=message.text
    bot.send_message(message.from_user.id, "Какой вы национальности(страна)?")
    bot.register_next_step_handler(message, registr_country)

def registr_country(message):
    global country
    country=message.text
    text=f"Вас зовут {name} {surname}, вам {age} и вы из {country}. Верно?"
    button=types.InlineKeyboardMarkup()
    button_yes=types.InlineKeyboardButton(text="Абсолютно верно", callback_data="Верно")
    button_no=types.InlineKeyboardButton(text="Нет", callback_data="Не верно")
    button.add(button_yes, button_no)
    bot.send_message(message.from_user.id, text=text, reply_markup=button)

@bot.callback_query_handler(func=lambda call: True)
def callbeck_handler(call):
    if call.data=="Верно":
        bot.send_message(call.message.chat.id, "Отлично! Приятно познакомиться)")
    elif call.data=="Не верно":
        bot.send_message(call.message.chat.id, "Тогда давайте познакомимся ещё раз) Как вас зовут?")
        bot.register_next_step_handler(call.message, registr_name)
