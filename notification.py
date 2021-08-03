import dotenv
import os
import smtplib
from email.mime.text import MIMEText

dotenv.load_dotenv()


class Notification:
    EMAIL_SENDER = os.getenv('EMAIL_SENDER')
    EMAIL_SENDER_PASSWORD = os.getenv('EMAIL_SENDER_PASSWORD')
    EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')
    SMTP_SERVER = os.getenv('SMTP_SERVER')

    SELL_NOTIFICATION_VALUE = os.getenv('SELL_NOTIFICATION_VALUE')
    BUY_NOTIFICATION_VALUE = os.getenv('BUY_NOTIFICATION_VALUE')
    CRYPTOS = os.getenv('CRYPTOS').split(",")

    def __init__(self, current_price_list):
        self.current_price_list = current_price_list
        if self.EMAIL_SENDER == '':
            raise ValueError("Missing `email_sender`.")

        if self.EMAIL_RECEIVER == '':
            raise ValueError("Missing `email_receiver`.")
        else:
            self.EMAIL_RECEIVER = self.EMAIL_RECEIVER.split(",")

        if self.EMAIL_SENDER_PASSWORD == '':
            raise ValueError("Missing `email_sender_password`.")
        if self.SMTP_SERVER == '':
            raise ValueError("Missing `smtp_server`.")

    def create_email_connection(self):
        gmail_user = self.EMAIL_SENDER
        gmail_password = self.EMAIL_SENDER_PASSWORD

        try:
            server = smtplib.SMTP_SSL(self.SMTP_SERVER, 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            return server
        except smtplib.SMTPAuthenticationError:
            print("Failed to authenticate user.")

    def send_email(self, buy, crypto, price):
        email_css = open("email.css").read()
        email_html = open("email.html").read()
        if buy:
            subject = "[B]Jmartins Crypto Notifier"
            body = email_html.format(email_css, crypto, price, "buying")

        else:
            subject = "[S]Jmartins Crypto Notifier"
            body = email_html.format(email_css, crypto, price, "selling")

        msg = MIMEText(body, 'html')
        msg['Subject'] = subject

        try:
            server = self.create_email_connection()
            server.send_message(msg, self.EMAIL_SENDER, self.EMAIL_RECEIVER)
            server.close()
            print("An Email has been sent!")
        except smtplib.SMTPRecipientsRefused:
            print("All recipients failed to receive email notification.")

    def sell_notification(self):
        if self.SELL_NOTIFICATION_VALUE == '':
            raise ValueError("Missing `sell_notification_value`.")
        else:
            self.SELL_NOTIFICATION_VALUE = self.SELL_NOTIFICATION_VALUE.split(",")

        for i in range(len(self.current_price_list)):
            if float(self.current_price_list[i]) >= float(self.SELL_NOTIFICATION_VALUE[i]):
                self.send_email(False, self.CRYPTOS[i], self.current_price_list[i])

    def buy_notification(self):
        if self.BUY_NOTIFICATION_VALUE == '':
            raise ValueError("Missing `buy_notification_value`.")
        else:
            self.BUY_NOTIFICATION_VALUE = self.BUY_NOTIFICATION_VALUE.split(",")

        for i in range(len(self.current_price_list)):
            if float(self.current_price_list[i]) <= float(self.BUY_NOTIFICATION_VALUE[i]):
                self.send_email(True, self.CRYPTOS[i], self.current_price_list[i])
