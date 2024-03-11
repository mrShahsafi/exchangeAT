import requests
from random import random
from backend.settings import EXCHANGE_URL


def buy_from_exchange(currency:str,amount:str) -> bool:
    print('buy_from_exchange',currency,amount)
    # response = requests.post(EXCHANGE_URL, json=data, headers=headers)
    return random() < 0.9
