import os
import sched
import time
import datetime
from crypto import Crypto
from notification import Notification
from environment import instantiate_environment


environment = instantiate_environment()

s = sched.scheduler(time.time, time.sleep)
crypto = Crypto(environment)
client = crypto.connect_coinbase()

last_message_sent = None


def retrieve_and_notify_price():
    global last_message_sent
    current_price_list = crypto.get_crypto_data(client)

    current_time = datetime.datetime.now()
    message_interval = datetime.timedelta(hours=int(environment['message_interval']))

    if last_message_sent is None or current_time > last_message_sent + message_interval:
        notification = Notification(current_price_list, environment)
        emails_sent = notification.compare_price_and_notify()
        if emails_sent == 1:
            print("1 email has been sent!")
        elif emails_sent > 1:
            print("{} emails has been sent!".format(emails_sent))
        else:
            return
        last_message_sent = current_time

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
            file.write("An error occurred at time: {} with the error: {}\n".format(datetime.datetime.now(), error))
            file.close()

            print("Error occurred: {}.".format(error))
            print("The program will try again.\n".format(environment['update_interval']))

            continue


if __name__ == "__main__":
    main()
