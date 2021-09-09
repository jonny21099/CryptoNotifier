import unittest
import dotenv
import os

from src.coinbase.notification import Notification
from unittest.mock import MagicMock

dotenv.load_dotenv()


class TestCoinbaseNotification(unittest.TestCase):
    test_environment = dict()
    price_list = ["4"]
    test_environment["email_sender"] = os.getenv("EMAIL_SENDER")
    test_environment["email_sender_password"] = os.getenv("EMAIL_SENDER_PASSWORD")
    test_environment["smtp_server"] = os.getenv("SMTP_SERVER")
    test_environment["email_receiver"] = ["test_receiver"]
    test_environment["cryptos"] = ["test_cryptos"]
    test_environment["buy_notification_value"] = ["5"]
    test_environment["sell_notification_value"] = ["3"]

    test_notification = Notification(price_list, test_environment)

    def test_notification_instantiation(self):
        assert(self.test_notification.current_price_list == self.price_list and
                self.test_notification.email_sender == self.test_environment["email_sender"] and
                self.test_notification.email_sender_password == self.test_environment["email_sender_password"] and
                self.test_notification.smtp_server == self.test_environment["smtp_server"] and
                self.test_notification.email_receiver == self.test_environment["email_receiver"] and
                self.test_notification.cryptos == self.test_environment["cryptos"] and
                self.test_notification.buy_notification_value == self.test_environment["buy_notification_value"] and
                self.test_notification.sell_notification_value == self.test_environment["sell_notification_value"])

    def test_send_buy_email(self):
        self.test_notification.send_email = MagicMock(return_value="TEST SEND BUY EMAIL")
        self.test_notification.buy_notification()
        self.test_notification.send_email.assert_called_once_with(True, self.test_environment["cryptos"][0],
                                                                  self.price_list[0])

    def test_send_sell_email(self):
        self.test_notification.send_email = MagicMock(return_value="TEST SEND SELL EMAIL")
        self.test_notification.sell_notification()
        self.test_notification.send_email.assert_called_once_with(False, self.test_environment["cryptos"][0],
                                                                  self.price_list[0])




