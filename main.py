import os
import sched
import time
import dotenv
from crypto import Crypto
from notification import Notification

dotenv.load_dotenv()

UPDATE_INTERVAL = os.getenv("UPDATE_INTERVAL")

if UPDATE_INTERVAL == '':
    raise ValueError("Missing `update_interval`")


def main():
    crypto = Crypto()

    current_price_list = crypto.get_crypto_price()

    notification = Notification(current_price_list)

    notification.buy_notification()

    notification.sell_notification()

    print('\n')


if __name__ == "__main__":
    print("Thank you for using Jmartins Crypto Notifier.\n\nThe program is now running.")
    while True:
        s = sched.scheduler(time.time, time.sleep)
        s.enter(int(UPDATE_INTERVAL), 1, main)
        s.run()
