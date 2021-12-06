import smtplib
import datetime
from email.mime.text import MIMEText


class NotificationSMTP:
    def __init__(self, current_price_list, environment):
        self.__current_price_list = current_price_list
        self.__email_sender = environment["email_sender"]
        self.__email_sender_password = environment["email_sender_password"]
        self.__smtp_server = environment["smtp_server"]
        self.__email_receiver = environment["email_receiver"]
        self.__cryptos = environment["cryptos"]
        self.__buy_notification_value = environment["buy_notification_value"]
        self.__sell_notification_value = environment["sell_notification_value"]
        self.__notification_cd_timer = environment["notification_cd_timer"]
        self.__notification_interval = environment["notification_interval"]

    def create_email_connection(self):
        try:
            server = smtplib.SMTP_SSL(self.__smtp_server, 465)
            server.ehlo()
            server.login(self.__email_sender, self.__email_sender_password)
            return server
        except smtplib.SMTPAuthenticationError:
            print("Failed to authenticate user.")

    def send_email(self, buy, crypto, price):
        email_css = open("../email/email.css").read()
        email_html = open("../email/email.html").read()
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
            server.send_message(msg, self.__email_sender, self.__email_receiver)
            server.close()
        except smtplib.SMTPRecipientsRefused:
            print("All recipients failed to receive email notification.")

    def compare_price_and_notify(self):
        emails_sent = 0
        for i in range(len(self.__current_price_list)):
            if float(self.__current_price_list[i]) >= float(self.__sell_notification_value[i]):
                print(f"The price of {self.__cryptos[i]} has reached {self.__current_price_list[i]}.")
                buy = False
            elif float(self.__current_price_list[i]) <= float(self.__buy_notification_value[i]):
                print(f"The price of {self.__cryptos[i]} has dropped to {self.__current_price_list[i]}.")
                buy = True
            else:
                continue
            if self.__notification_cd_timer[i] is None or self.__notification_cd_timer[i] + datetime.timedelta(
                    hours=self.__notification_interval) <= datetime.datetime.now():
                self.send_email(buy, self.__cryptos[i], self.__current_price_list[i])
                self.__notification_cd_timer[i] = datetime.datetime.now()
            emails_sent += 1
        return emails_sent
