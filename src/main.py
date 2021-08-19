import os
import sched
import time
from datetime import datetime
from crypto import Crypto
from notification import Notification
from environment import instantiate_environment


environment = instantiate_environment()

s = sched.scheduler(time.time, time.sleep)
crypto = Crypto(environment['coinbase_api_key'], environment['coinbase_secret_key'],
                environment['currency'], environment['cryptos'])
client = crypto.connect_coinbase()


def retrieve_and_notify_price():
    current_price_list = crypto.get_crypto_price(client)

    notification = Notification(current_price_list, environment['email_sender'], environment['email_sender_password'],
                                environment['smtp_server'], environment['email_receiver'], environment['cryptos'],
                                environment['buy_notification_value'], environment['sell_notification_value'])
    notification.buy_notification()
    notification.sell_notification()

    print('\n')


def main():
    if os.path.exists("error.txt"):
        os.remove("error.txt")

    print("Thank you for using Jmartins Crypto Notifier.\n\nThe program is now running.")

    while True:
        try:
            s.enter(int(environment['update_interval']), 1, retrieve_and_notify_price)
            s.run()

        except Exception as error:
            file = open("error.txt", "a")
            file.write("An error occurred at time: {} with the error: {}\n".format(datetime.now(), error))
            file.close()

            print("Error occurred: {}.".format(error))
            print("The program will try again.\n".format(environment['update_interval']))

            continue


if __name__ == "__main__":
    main()
