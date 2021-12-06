import boto3
import datetime
from notification_utils import NotificationUtils


class NotificationSNS:
    def __init__(self, current_price_list, environment):
        self.__current_price_list = current_price_list
        self.__cryptos = environment["cryptos"]
        self.__buy_notification_value = environment["buy_notification_value"]
        self.__sell_notification_value = environment["sell_notification_value"]
        self.__topic_arn = environment["topic_arn"]
        self.__currency = environment["currency"]
        self.__notification_cd_timer = environment["notification_cd_timer"]
        self.__notification_interval = environment["notification_interval"]

    def compare_price_and_notify(self):
        emails_sent = 0
        for i in range(len(self.__current_price_list)):
            buy = NotificationUtils.compare_price(self.__current_price_list[i], self.__sell_notification_value[i],
                                                  self.__buy_notification_value[i], self.__cryptos[i])
            if buy is None:
                continue

            if self.__notification_cd_timer[i] is None or self.__notification_cd_timer[i] + datetime.timedelta(
                    hours=self.__notification_interval) <= datetime.datetime.now():
                self.publish_notification(buy, self.__cryptos[i], self.__current_price_list[i])
                self.__notification_cd_timer[i] = datetime.datetime.now()
                emails_sent += 1

        return emails_sent

    def publish_notification(self, buy, crypto, current_value):
        client = boto3.client('sns')
        message = f"{crypto} has reached the price of ${current_value}{self.__currency}."
        if buy:
            message += " Time to pull out the wallet and buy more."
        else:
            message += " Working our way to Bugattis."
        response = client.publish(
            TopicArn=f'{self.__topic_arn}',
            Message=message,
        )
        return response
