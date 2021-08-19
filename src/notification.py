import smtplib
from email.mime.text import MIMEText


class Notification:
    def __init__(self, current_price_list, email_sender, email_sender_password, smtp_server,
                 email_receiver, cryptos, buy_notification_value, sell_notification_value):
        self.current_price_list = current_price_list
        self.email_sender = email_sender
        self.email_sender_password = email_sender_password
        self.smtp_server = smtp_server
        self.email_receiver = email_receiver
        self.cryptos = cryptos
        self.buy_notification_value = buy_notification_value
        self.sell_notification_value = sell_notification_value

    def create_email_connection(self):
        try:
            server = smtplib.SMTP_SSL(self.smtp_server, 465)
            server.ehlo()
            server.login(self.email_sender, self.email_sender_password)
            return server
        except smtplib.SMTPAuthenticationError:
            print("Failed to authenticate user.")

    def send_email(self, buy, crypto, price):
        email_css = open("src/email.css").read()
        email_html = open("src/email.html").read()
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
            server.send_message(msg, self.email_sender, self.email_receiver)
            server.close()
            print("An Email has been sent!")
        except smtplib.SMTPRecipientsRefused:
            print("All recipients failed to receive email notification.")

    def sell_notification(self):
        for i in range(len(self.current_price_list)):
            if float(self.current_price_list[i]) >= float(self.sell_notification_value[i]):
                self.send_email(False, self.cryptos[i], self.current_price_list[i])

    def buy_notification(self):
        for i in range(len(self.current_price_list)):
            if float(self.current_price_list[i]) <= float(self.buy_notification_value[i]):
                self.send_email(True, self.cryptos[i], self.current_price_list[i])
