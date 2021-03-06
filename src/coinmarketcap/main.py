import datetime
import sched
import time

from crypto import Crypto
from environment import *
from notification_sns import NotificationSNS
from notification_smtp import NotificationSMTP

Environment()

s = sched.scheduler(time.time, time.sleep)
crypto = Crypto(Environment.environment)


def retrieve_and_notify_price():
    current_price_list = crypto.get_crypto_quote()
    notification = NotificationSNS(current_price_list, Environment.environment) \
        if Environment.environment['notification_type'] == "SNS" \
        else NotificationSMTP(current_price_list, Environment.environment)
    emails_sent = notification.compare_price_and_notify()
    if emails_sent >= 1:
        print(f"{emails_sent} {Environment.environment['notification_type']} "
              f"{'notification' if emails_sent == 1 else 'notifications'} "
              f"{'has' if emails_sent == 1 else 'have'} been sent!")
    else:
        return
    print('\n')


def main():
    if os.path.exists("error.txt"):
        os.remove("error.txt")

    print("Thank you for using Jmartins Crypto Notifier.\n\nThe program is now running.")
    retrieve_and_notify_price()

    while True:
        try:
            s.enter(Environment.environment['update_interval'], 1, retrieve_and_notify_price)
            s.run()

        except Exception as error:
            file = open("error.txt", "a")
            file.write(f"An error occurred at time: {datetime.datetime.now()} with the error: {error}\n")
            file.close()

            print(f"Error occurred: {error}.")
            print(f"The program will try again.\n")

            continue


if __name__ == "__main__":
    main()
