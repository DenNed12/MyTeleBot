from utils import CriptoConverter, ConvertionError
import telebot
from config import TOKEN, val


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands= ['start','help'])
def command_handler(message: telebot.types.Message):
    text = f"""Я умею выводить и конвертировать  валюты и криптовалюты, для того чтобы конвертировать вам  нужно написать исходную валюту, валюту конвертации и количество
    Например : эфириум доллар 1 - для конвертирования 1 единицы эфириума в доллары"""
    bot.reply_to(message,text)

@bot.message_handler(commands = ["values"])
def print_val(message:telebot.types.Message):
    string = "Доступные валюты:"

    for v in val.keys():
        string = "\n".join((string,v))
    bot.reply_to(message,string)


@bot.message_handler(content_types=["text"])
def convert(message:telebot.types.Message):
    values = message.text.split(" ")

    if len(values) != 3:
        raise ConvertionError("Укажите 3 параметра: исходная валюта, валюта конвертации и количество")
    quote,base,amount = values
    total_base = CriptoConverter.convert(quote,base,amount)

    text = f"Цена {amount} {quote} в {base} равна {total_base}"
    bot.send_message(message.chat.id,text)


bot.polling(none_stop=True)