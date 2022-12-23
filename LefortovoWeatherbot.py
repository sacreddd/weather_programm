import config
import telebot
import graphcreate
import os
import time

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>ну привет</b>', parse_mode='html')


@bot.message_handler(commands=['getWeather'])
def getWeather(message):
    data = message.text.split()[1]
    graphcreate.gdraw(data)
    file = open(f'{data}.png','rb')
    bot.send_photo(message.chat.id, file, f'<b>Погода на {data} по часам</b>', parse_mode='html')
    file.close()
    path = f'C:\\Users\\stas_mashina\\Documents\\доки\\weather_programm\\{data}.png'
    os.remove(path)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'<b>/getWeather</b> - погода на конкретную дату \n (/getWeather ГГГГ-ММ-ДД)', parse_mode='html')


bot.polling(none_stop=True)
