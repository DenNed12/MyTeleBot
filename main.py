import requests
import json
import telebot

TOKEN = "6370602328:AAHs-ITUhEb7AEsifm4QN_zTJ52F78HTsaU"
bot = telebot.TeleBot(TOKEN)

val = {
    "эфириум":"ETH",
    "биткоин":"BTC",
    "доллар":"USD",
    "евро":"EUR"
}

class ConvertionError(Exception):
    pass



@bot.message_handler(commands= ['start','help'])
def command_handler(message: telebot.types.Message):
    text =  f"""Я умею конвертировать и выводить  валюты 
    и криптовалюты, для того чтобы конвертировать - нужно написать исходную валюту, валюту конвертации и количество """
    bot.reply_to(message,text)

@bot.message_handler(commands = ["values"])
def print_val(message:telebot.types.Message):
    string = "Доступные валюты:"

    for v in val.keys():
        string = "\n".join((string,v))
    bot.reply_to(message,string)

# @bot.message_handler(content_types = ["text"])
# def message_handler(message: telebot.types.Message):
#     if message.text == "привет" or message.text == "Привет":
#         bot.reply_to(message, f"Привет {message.chat.first_name}, рад тебя видеть!")

@bot.message_handler(content_types=["text"])
def convert(message:telebot.types.Message):
    quote, base, amount = message.text.split(" ")
    r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={val[quote]}&tsyms={val[base]}")
    text = json.loads(r.content)[val[base]] * int(amount)
    bot.send_message(message.chat.id,text)




bot.polling(none_stop=True)