import requests
import json
import telebot

TOKEN = "6370602328:AAHs-ITUhEb7AEsifm4QN_zTJ52F78HTsaU"
bot  = telebot.TeleBot(TOKEN)

val = {
   "эфириум" : "ETH",
    "биткоин": "BTC",
    "доллар": "USD"
}

@bot.message_handler(command= ['start','help'])
def command_handler(message: telebot.types.Message):
    text =  f"""Я умею конвертировать и выводить  валюты 
    и криптовалюты, для того чтобы конвертировать, нужно написать : """
    bot.reply_to(message,text)


# @bot.message_handler(content_types =["text",])
# def message_handler(message: telebot.types.Message):
#     bot.reply_to(message , f"Привет {message.chat.first_name}, я рад тебя видеть!")


bot.polling()