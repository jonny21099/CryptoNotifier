from datetime import datetime
from coinbase.wallet.client import Client
from colorama import Fore, Back, Style


class Crypto:
    def __init__(self, environment):
        self.api_key = environment["api_key"]
        self.api_secret = environment["api_secret"]
        self.currency = environment["currency"]
        self.cryptos = environment["cryptos"]

    def connect_coinbase(self):
        client = Client(self.api_key, self.api_secret)
        return client

    def get_crypto_data(self, client):
        current_price_list = []
        total_profit = 0
        total_balance = 0
        print("Fetching prices...")
        print("Retrieval time: {}\n".format(datetime.now()))
        for crypto in self.cryptos:
            price = client.get_spot_price(currency_pair=crypto + "-" + self.currency)
            holding = client.get_account(crypto)
            buy_history = client.get_buys(crypto)
            sell_history = client.get_sells(crypto)

            crypto_profit = self.get_profit(holding, buy_history, sell_history)

            message = self.format_log_message(price, holding, crypto_profit)
            print(message)
            print(Style.RESET_ALL)

            current_price_list.append(price['amount'])

            total_balance += float(holding.native_balance.amount)
            total_profit += crypto_profit

        print("Total Balance: ${}".format(total_balance))

        if total_profit >= 0:
            profit_message = Fore.GREEN + "Total Profit: ${}".format(total_profit)
        else:
            profit_message = Fore.RED + "Total Profit: ${}".format(total_profit)

        print(profit_message)
        print(Style.RESET_ALL)

        return current_price_list

    @staticmethod
    def get_profit(holding, buy_history, sell_history):
        buy_total = 0
        sell_total = 0
        crypto_balance = float(holding.native_balance.amount)

        for index, purchase in enumerate(buy_history.data):
            buy_total += float(purchase.total.amount) if purchase.status == "completed" else 0

        for index, sold in enumerate(sell_history.data):
            sell_total += float(sold.total.amount) if sold.status == "completed" else 0

        return crypto_balance + (sell_total - buy_total)

    @staticmethod
    def format_log_message(price, holding, crypto_profit):
        if crypto_profit >= 0:
            profit_message = Fore.GREEN + "Profit: ${}".format(crypto_profit)
        else:
            profit_message = Fore.RED + "Profit: ${}".format(crypto_profit)

        message = "Asset: {}\n".format(price.base) \
                  + "Currency: {}\n".format(price.currency) \
                  + "Holding: {}\n".format(holding.balance.amount) \
                  + "Price: ${}\n".format(price.amount) \
                  + "Balance: ${}\n".format(holding.native_balance.amount) \
                  + profit_message

        return message
