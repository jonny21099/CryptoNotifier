import dotenv
import os
import argparse

dotenv.load_dotenv()

environment = dict()

environment["update_interval"] = os.getenv("UPDATE_INTERVAL")
environment["message_interval"] = os.getenv("MESSAGE_INTERVAL")

environment["api_key"] = os.getenv('CMC_PRO_API_KEY')

environment["currency"] = os.getenv('CURRENCY')
environment["cryptos"] = os.getenv('CRYPTOS')

environment["topic_arn"] = os.getenv("SNS_TOPIC_ARN")

environment["email_sender"] = os.getenv('EMAIL_SENDER')
environment["email_sender_password"] = os.getenv('EMAIL_SENDER_PASSWORD')
environment["email_receiver"] = os.getenv('EMAIL_RECEIVER')
environment["smtp_server"] = os.getenv('SMTP_SERVER')

environment["sell_notification_value"] = os.getenv('SELL_NOTIFICATION_VALUE')
environment["buy_notification_value"] = os.getenv('BUY_NOTIFICATION_VALUE')


def email_method():
    parser = argparse.ArgumentParser(description='Send message through SMTP or SNS.')
    parser.add_argument('email_method', type=str, nargs=1,
                        help='SMTP or SNS.')
    args = parser.parse_args()
    return args.email_method[0].upper() if args.email_method[0].upper() == "SMTP" or args.email_method[0].upper() == "SNS" else None


def instantiate_environment():
    method = email_method()
    if method == "SMTP":
        verify_smtp()
    elif method == "SNS":
        verify_sns()

    if environment["update_interval"] == '':
        raise ValueError("Missing `update_interval`")

    if environment["message_interval"] == '':
        raise ValueError("Missing `message_interval`")

    if environment["currency"] == '':
        raise ValueError("Missing `currency`.")

    if environment["cryptos"] == '':
        raise ValueError("Missing `cryptos`.")
    else:
        environment["cryptos"] = environment["cryptos"].split(",")

    if environment["sell_notification_value"] == '':
        raise ValueError("Missing `sell_notification_value`.")
    else:
        environment["sell_notification_value"] = environment["sell_notification_value"].split(",")

    if environment["buy_notification_value"] == '':
        raise ValueError("Missing `buy_notification_value`.")
    else:
        environment["buy_notification_value"] = environment["buy_notification_value"].split(",")

    return environment


def verify_smtp():
    if environment["email_sender"] == '':
        raise ValueError("Missing `email_sender`.")

    if environment["email_receiver"] == '':
        raise ValueError("Missing `email_receiver`.")
    else:
        environment["email_receiver"] = environment["email_receiver"].split(",")

    if environment["email_sender_password"] == '':
        raise ValueError("Missing `email_sender_password`.")

    if environment["smtp_server"] == '':
        raise ValueError("Missing `smtp_server`.")


def verify_sns():
    if environment["topic_arn"] == '':
        raise ValueError("Missing `topic_arn`.")
