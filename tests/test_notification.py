import unittest
import dotenv
import os

from src.notification import Notification
from unittest.mock import MagicMock

dotenv.load_dotenv()


class TestNotification(unittest.TestCase):
    price_list = ["4"]
    sender = os.getenv("EMAIL_SENDER")
    sender_pass = os.getenv("EMAIL_SENDER_PASSWORD")
    server = os.getenv("SMTP_SERVER")
    receiver = ["test_receiver"]
    cryptos = ["test_cryptos"]
    buy_value = ["5"]
    sell_value = ["3"]

    test_notification = Notification(price_list, sender, sender_pass, server, receiver, cryptos,
                                     buy_value, sell_value)

    def test_notification_instantiation(self):
        assert(self.test_notification.current_price_list == self.price_list and
                self.test_notification.email_sender == self.sender and
                self.test_notification.email_sender_password == self.sender_pass and
                self.test_notification.smtp_server == self.server and
                self.test_notification.email_receiver == self.receiver and
                self.test_notification.cryptos == self.cryptos and
                self.test_notification.buy_notification_value == self.buy_value and
                self.test_notification.sell_notification_value == self.sell_value)

    def test_send_buy_email(self):
        self.test_notification.send_email = MagicMock(return_value="TEST SEND BUY EMAIL")
        self.test_notification.buy_notification()
        self.test_notification.send_email.assert_called_once_with(True, self.cryptos[0], self.price_list[0])

    def test_send_sell_email(self):
        self.test_notification.send_email = MagicMock(return_value="TEST SEND SELL EMAIL")
        self.test_notification.sell_notification()
        self.test_notification.send_email.assert_called_once_with(False, self.cryptos[0], self.price_list[0])




