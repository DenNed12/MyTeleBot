import requests
import json
from config import val
class ConvertionError(Exception):
    pass

class CriptoConverter:
    @staticmethod
    def convert(quote: str,base: str,amount:str):

        if quote == base:
            raise ConvertionError("Укажите две разные валюты!")

        try:
            quote_ticker = val[quote]
        except KeyError:
            raise ConvertionError(f"Не удалось обработать валюту {quote}")

        try:
            base_ticker = val[base]
        except:
            raise ConvertionError(f"Не удалось обработать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionError(f"Не удалось обработать количество {amount}")

        finally:
            #r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
            r = requests.get(f" https://v6.exchangerate-api.com/v6/8882e2bf256b8996a2a24927/pair/{quote_ticker}/{base_ticker}/{amount}")
            print(r.text)
            total_base = json.loads(r.content)["conversion_result"] #* int(amount)
            print(total_base)
            return total_base


