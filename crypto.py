import os
import dotenv
from coinbase.wallet.client import Client

dotenv.load_dotenv()


class Crypto:
    COINBASE_API_KEY = os.getenv('COINBASE_API_KEY')
    COINBASE_SECRET_KEY = os.getenv('COINBASE_SECRET_KEY')

    CURRENCY = os.getenv('CURRENCY')
    CRYPTOS = os.getenv('CRYPTOS').split(",")

    current_price_list = []

    def connect_coinbase(self):
        self.current_price_list = []
        client = Client(self.COINBASE_API_KEY, self.COINBASE_SECRET_KEY)
        return client

    def get_crypto_price(self):
        client = self.connect_coinbase()
        for crypto in self.CRYPTOS:
            price = client.get_spot_price(currency_pair=crypto + "-" + self.CURRENCY)
            self.current_price_list.append(price['amount'])
        return self.current_price_list
