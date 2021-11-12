import smtplib
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
                self.send_email(False, self.__cryptos[i], self.__current_price_list[i])
            elif float(self.__current_price_list[i]) <= float(self.__buy_notification_value[i]):
                self.send_email(True, self.__cryptos[i], self.__current_price_list[i])
            else:
                continue
            emails_sent += 1
        return emails_sent
