import requests
import json
from config import *

class ExchangeException(Exception):
    pass


class Exchange:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if quote == base:
            raise ExchangeException(f'Нельзя конвертировать одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise ExchangeException(f'Не смог обработать валюту {quote.lower()}')

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise ExchangeException(f'Не смог обработать валюту {base.lower()}')

        try:
            amount = float(amount)
        except ValueError:
            raise ExchangeException(f'Не смог обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = float(json.loads(r.content)[keys[quote.lower()]])
        return round(total_base*amount, 6) #Округление после запятой
    
