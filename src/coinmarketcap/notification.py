import boto3


class Notification:
    def __init__(self, current_price_list, environment):
        self.__current_price_list = current_price_list
        self.__cryptos = environment["cryptos"]
        self.__buy_notification_value = environment["buy_notification_value"]
        self.__sell_notification_value = environment["sell_notification_value"]
        self.__topic_arn = environment["topic_arn"]
        self.__currency = environment["currency"]

    def compare_price_and_notify(self):
        emails_sent = 0
        for i in range(len(self.__current_price_list)):
            if float(self.__current_price_list[i]) >= float(self.__sell_notification_value[i]):
                self.publish_notification(False, self.__cryptos[i], self.__current_price_list[i])
            elif float(self.__current_price_list[i]) <= float(self.__buy_notification_value[i]):
                self.publish_notification(True, self.__cryptos[i], self.__current_price_list[i])
            else:
                continue
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
