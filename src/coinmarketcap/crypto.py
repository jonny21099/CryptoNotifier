from datetime import datetime
import requests


class Crypto:
    def __init__(self, environment):
        self.api_key = environment["api_key"]
        self.currency = environment["currency"]
        self.cryptos = environment["cryptos"]

    def get_crypto_quote(self):
        current_price_list = []

        URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
        PARAMS = {"CMC_PRO_API_KEY": self.api_key, "symbol": ",".join(self.cryptos), "convert": self.currency}

        print("Fetching prices...")
        r = requests.get(URL, PARAMS)
        data = r.json()
        print("Retrieval time: {}\n".format(datetime.now()))

        for crypto in self.cryptos:
            price = data['data'][crypto]["quote"][self.currency]["price"]
            current_price_list.append(price)
            print(self.format_log_message(crypto, price))

        return current_price_list

    def format_log_message(self, crypto, price):
        message = "Asset: {}\n".format(crypto) \
                  + "Currency: {}\n".format(self.currency) \
                  + "Price: ${}\n".format(price)
        return message


