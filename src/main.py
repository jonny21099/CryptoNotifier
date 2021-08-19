import os
import sched
import time
from datetime import datetime
from crypto import Crypto
from notification import Notification
from environment import instantiate_environment

update_interval, coinbase_api_key, coinbase_secret_key, currency, cryptos, email_sender, email_sender_password, \
email_receiver, smtp_server, sell_notification_value, buy_notification_value = instantiate_environment()

s = sched.scheduler(time.time, time.sleep)
crypto = Crypto(coinbase_api_key, coinbase_secret_key, currency, cryptos)
client = crypto.connect_coinbase()


def retrieve_and_notify_price():
    current_price_list = crypto.get_crypto_price(client)

    notification = Notification(current_price_list, email_sender, email_sender_password, smtp_server, email_receiver,
                                cryptos, buy_notification_value, sell_notification_value)
    notification.buy_notification()
    notification.sell_notification()

    print('\n')


def main():
    if os.path.exists("error.txt"):
        os.remove("error.txt")

    print("Thank you for using Jmartins Crypto Notifier.\n\nThe program is now running.")

    while True:
        try:
            s.enter(int(update_interval), 1, retrieve_and_notify_price)
            s.run()

        except Exception as error:
            file = open("error.txt", "a")
            file.write("An error occurred at time: {} with the error: {}\n".format(datetime.now(), error))
            file.close()

            print("Error occurred: {}.".format(error))
            print("The program will try again.\n".format(update_interval))

            continue


if __name__ == "__main__":
    main()
