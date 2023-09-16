import requests
import json
import telebot

TOKEN = "6370602328:AAHs-ITUhEb7AEsifm4QN_zTJ52F78HTsaU"
bot = telebot.TeleBot(TOKEN)

val = {
   "эфириум" : "ETH",
    "биткоин": "BTC",
    "доллар": "USD"
}

class ConvertionError(Exception):
    pass



@bot.message_handler(commands= ['start','help'])
def command_handler(message: telebot.types.Message):
    text =  f"""Я умею конвертировать и выводить  валюты 
    и криптовалюты, для того чтобы конвертировать, нужно написать : """
    bot.reply_to(message,text)


@bot.message_handler(content_types =["text",])
def message_handler(message: telebot.types.Message):
    bot.reply_to(message , f"Привет {message.chat.first_name}, я рад тебя видеть!")



@bot.message_handler(content_types = ["text",])
def converter(message:telebot.types.Message):
    values = message.text.split()
    if len(values) != 3:
        raise ConvertionError("Слишком много параметров")
    quote,base,amount = values
    r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={val[quote]}&tsyms={val[base]},JPY,EUR")
    total_base = json.loads(r.content)[val[base]]
    text = f"Цена {amount} {quote} в {base} равна  {total_base}"
    bot.send_message(message.chat.id, text)

bot.polling()