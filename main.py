import os
import sched
import smtplib
import time
from email.mime.text import MIMEText

import dotenv
from coinbase.wallet.client import Client

dotenv.load_dotenv()

UPDATE_INTERVAL = os.getenv("UPDATE_INTERVAL")

COINBASE_API_KEY = os.getenv('COINBASE_API_KEY')
COINBASE_SECRET_KEY = os.getenv('COINBASE_SECRET_KEY')

CURRENCY = os.getenv('CURRENCY')
CRYPTOS = os.getenv('CRYPTOS').split(",")

SELL_NOTIFICATION_VALUE = os.getenv('SELL_NOTIFICATION_VALUE').split(",")
BUY_NOTIFICATION_VALUE = os.getenv('BUY_NOTIFICATION_VALUE').split(",")

EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_SENDER_PASSWORD = os.getenv('EMAIL_SENDER_PASSWORD')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER').split(",")
SMTP_SERVER = os.getenv('SMTP_SERVER')

current_price_list = []


def connect_coinbase():
    global current_price_list
    current_price_list = []
    client = Client(COINBASE_API_KEY, COINBASE_SECRET_KEY)
    return client


def get_crypto_price(client):
    for crypto in CRYPTOS:
        price = client.get_spot_price(currency_pair=crypto + "-" + CURRENCY)
        current_price_list.append(price['amount'])


def sell_notification():
    for i in range(len(current_price_list)):
        if float(current_price_list[i]) >= float(SELL_NOTIFICATION_VALUE[i]):
            send_email(False, CRYPTOS[i], current_price_list[i])


def buy_notification():
    for i in range(len(current_price_list)):
        if float(current_price_list[i]) <= float(BUY_NOTIFICATION_VALUE[i]):
            send_email(True, CRYPTOS[i], current_price_list[i])


def create_email_connection():
    gmail_user = EMAIL_SENDER
    gmail_password = EMAIL_SENDER_PASSWORD

    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        return server
    except smtplib.SMTPAuthenticationError:
        print("Failed to authenticate user.")


def send_email(buy, crypto, price):
    if buy:
        subject = "[B]Jmartins Crypto Notifier"
        body = "You setup an alert with Jmartins Crypto Notifier.\n\n" \
               "{} has reached ${}, and is lower than your expected purchase price.".format(crypto, price)
    else:
        subject = "[S]Jmartins Crypto Notifier"
        body = "You setup an alert with Jmartins Crypto Notifier.\n\n" \
               "{} has reached ${}, and is higher than your expected selling price.".format(crypto, price)

    msg = MIMEText(body)
    msg['Subject'] = subject

    try:
        server = create_email_connection()
        server.send_message(msg, EMAIL_SENDER, EMAIL_RECEIVER)
        server.close()
        print("An Email has been sent!")
    except smtplib.SMTPRecipientsRefused:
        print("All recipients failed to receive email notification.")


def main():
    client = connect_coinbase()

    get_crypto_price(client)

    buy_notification()

    sell_notification()


if __name__ == "__main__":
    print("Thank you for using Jmartins Crypto Notifier.\n\nThe program is now running.")
    while True:
        s = sched.scheduler(time.time, time.sleep)
        s.enter(int(UPDATE_INTERVAL), 1, main)
        s.run()
