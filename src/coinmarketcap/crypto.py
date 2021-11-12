from datetime import datetime
import requests


class Crypto:
    def __init__(self, environment):
        self.__api_key = environment["api_key"]
        self.__currency = environment["currency"]
        self.__cryptos = environment["cryptos"]

    def get_crypto_quote(self):
        current_price_list = []

        URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
        PARAMS = {"CMC_PRO_API_KEY": self.__api_key, "symbol": ",".join(self.__cryptos), "convert": self.__currency}

        print("Fetching prices...")
        r = requests.get(URL, PARAMS)
        data = r.json()
        print(f"Retrieval time: {datetime.now()}\n")

        for crypto in self.__cryptos:
            price = data['data'][crypto]["quote"][self.__currency]["price"]
            current_price_list.append(price)
            print(self.format_log_message(crypto, price))

        return current_price_list

    def format_log_message(self, crypto, price):
        message = f"Asset: {crypto}\n" \
                  + f"Currency: {self.__currency}\n" \
                  + f"Price: ${price}\n"
        return message


