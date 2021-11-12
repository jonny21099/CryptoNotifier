import dotenv
import os
import argparse

dotenv.load_dotenv()


class Environment:
    environment = dict()

    def __init__(self):
        self.environment["update_interval"] = os.getenv("UPDATE_INTERVAL")
        self.environment["message_interval"] = os.getenv("MESSAGE_INTERVAL")

        self.environment["api_key"] = os.getenv('CMC_PRO_API_KEY')

        self.environment["currency"] = os.getenv('CURRENCY')
        self.environment["cryptos"] = os.getenv('CRYPTOS')

        self.environment["topic_arn"] = os.getenv("SNS_TOPIC_ARN")

        self.environment["email_sender"] = os.getenv('EMAIL_SENDER')
        self.environment["email_sender_password"] = os.getenv('EMAIL_SENDER_PASSWORD')
        self.environment["email_receiver"] = os.getenv('EMAIL_RECEIVER')
        self.environment["smtp_server"] = os.getenv('SMTP_SERVER')

        self.environment["sell_notification_value"] = os.getenv('SELL_NOTIFICATION_VALUE')
        self.environment["buy_notification_value"] = os.getenv('BUY_NOTIFICATION_VALUE')

        self.environment["notification_type"] = self.__instantiate_environment()

    def __instantiate_environment(self):
        method = self.__get_notification_type()
        if method == "SMTP":
            # verify smtp env variables
            self.__verify_smtp()
        elif method == "SNS":
            # verify sns env variables
            self.__verify_sns()
        # verify all configuration env variables
        self.__verify_configuration()
        return method

    def __verify_smtp(self):
        if self.environment["email_sender"] == '':
            raise ValueError("Missing `email_sender`.")

        if self.environment["email_receiver"] == '':
            raise ValueError("Missing `email_receiver`.")
        else:
            self.environment["email_receiver"] = self.environment["email_receiver"].split(",")

        if self.environment["email_sender_password"] == '':
            raise ValueError("Missing `email_sender_password`.")

        if self.environment["smtp_server"] == '':
            raise ValueError("Missing `smtp_server`.")

    def __verify_sns(self):
        if self.environment["topic_arn"] == '':
            raise ValueError("Missing `topic_arn`.")

    def __verify_configuration(self):
        if self.environment["update_interval"] == '':
            raise ValueError("Missing `update_interval`")

        if self.environment["message_interval"] == '':
            raise ValueError("Missing `message_interval`")

        if self.environment["currency"] == '':
            raise ValueError("Missing `currency`.")

        if self.environment["cryptos"] == '':
            raise ValueError("Missing `cryptos`.")
        else:
            self.environment["cryptos"] = self.environment["cryptos"].split(",")

        if self.environment["sell_notification_value"] == '':
            raise ValueError("Missing `sell_notification_value`.")
        else:
            self.environment["sell_notification_value"] = self.environment["sell_notification_value"].split(",")

        if self.environment["buy_notification_value"] == '':
            raise ValueError("Missing `buy_notification_value`.")
        else:
            self.environment["buy_notification_value"] = self.environment["buy_notification_value"].split(",")

    @staticmethod
    def __get_notification_type():
        parser = argparse.ArgumentParser(description='Send message through SMTP or SNS.')
        parser.add_argument('email_method', choices=["SNS", "SMTP", "smtp", "sns"], type=str, nargs=1,
                            help='SMTP or SNS.')
        args = parser.parse_args()
        return args.email_method[0].upper() if args.email_method[0].upper() == "SMTP" or \
                                               args.email_method[0].upper() == "SNS" else None
