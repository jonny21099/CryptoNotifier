import dotenv
import os
import smtplib
from email.mime.text import MIMEText


class Notification:
    dotenv.load_dotenv()
    EMAIL_SENDER = os.getenv('EMAIL_SENDER')
    EMAIL_SENDER_PASSWORD = os.getenv('EMAIL_SENDER_PASSWORD')
    EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER').split(",")
    SMTP_SERVER = os.getenv('SMTP_SERVER')

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
            server = self.create_email_connection()
            server.send_message(msg, self.EMAIL_SENDER, self.EMAIL_RECEIVER)
            server.close()
            print("An Email has been sent!")
        except smtplib.SMTPRecipientsRefused:
            print("All recipients failed to receive email notification.")

    def sell_notification(self, current_price_list, sell_notification_value, cryptos):
        for i in range(len(current_price_list)):
            if float(current_price_list[i]) >= float(sell_notification_value[i]):
                self.send_email(False, cryptos[i], current_price_list[i])

    def buy_notification(self, current_price_list, buy_notification_value, cryptos):
        for i in range(len(current_price_list)):
            if float(current_price_list[i]) <= float(buy_notification_value[i]):
                self.send_email(True, cryptos[i], current_price_list[i])
