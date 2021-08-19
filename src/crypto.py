from datetime import datetime
from coinbase.wallet.client import Client


class Crypto:
    def __init__(self, api_key, api_secret, currency, cryptos):
        self.api_key = api_key
        self.api_secret = api_secret
        self.currency = currency
        self.cryptos = cryptos

    def connect_coinbase(self):
        client = Client(self.api_key, self.api_secret)
        return client

    def get_crypto_price(self, client):
        current_price_list = []
        print("Fetching prices...")
        print("Retrieval time: {}".format(datetime.now()))
        for crypto in self.cryptos:
            price = client.get_spot_price(currency_pair=crypto + "-" + self.currency)
            print(price)
            current_price_list.append(price['amount'])
        return current_price_list
