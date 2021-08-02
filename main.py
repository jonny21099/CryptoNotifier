import os
import sched
import time

import dotenv
from coinbase.wallet.client import Client
from notification import Notification

dotenv.load_dotenv()

UPDATE_INTERVAL = os.getenv("UPDATE_INTERVAL")

COINBASE_API_KEY = os.getenv('COINBASE_API_KEY')
COINBASE_SECRET_KEY = os.getenv('COINBASE_SECRET_KEY')

CURRENCY = os.getenv('CURRENCY')
CRYPTOS = os.getenv('CRYPTOS').split(",")

SELL_NOTIFICATION_VALUE = os.getenv('SELL_NOTIFICATION_VALUE').split(",")
BUY_NOTIFICATION_VALUE = os.getenv('BUY_NOTIFICATION_VALUE').split(",")

current_price_list = []


def connect_coinbase():
    global current_price_list
    current_price_list = []
    client = Client(COINBASE_API_KEY, COINBASE_SECRET_KEY)
    return client


def get_crypto_price(client):
    for crypto in CRYPTOS:
        price = client.get_spot_price(currency_pair=crypto + "-" + CURRENCY)
        current_price_list.append(price['amount'])


def main():
    client = connect_coinbase()

    get_crypto_price(client)

    notification = Notification()

    notification.buy_notification(current_price_list, BUY_NOTIFICATION_VALUE, CRYPTOS)

    notification.sell_notification(current_price_list, SELL_NOTIFICATION_VALUE, CRYPTOS)


if __name__ == "__main__":
    print("Thank you for using Jmartins Crypto Notifier.\n\nThe program is now running.")
    while True:
        s = sched.scheduler(time.time, time.sleep)
        s.enter(int(UPDATE_INTERVAL), 1, main)
        s.run()
