import dotenv
import os

dotenv.load_dotenv()

environment = dict()

environment["update_interval"] = os.getenv("UPDATE_INTERVAL")

environment["coinbase_api_key"] = os.getenv('COINBASE_API_KEY')
environment["coinbase_secret_key"] = os.getenv('COINBASE_SECRET_KEY')

environment["currency"] = os.getenv('CURRENCY')
environment["cryptos"] = os.getenv('CRYPTOS')

environment["email_sender"] = os.getenv('EMAIL_SENDER')
environment["email_sender_password"] = os.getenv('EMAIL_SENDER_PASSWORD')
environment["email_receiver"] = os.getenv('EMAIL_RECEIVER')
environment["smtp_server"] = os.getenv('SMTP_SERVER')

environment["sell_notification_value"] = os.getenv('SELL_NOTIFICATION_VALUE')
environment["buy_notification_value"] = os.getenv('BUY_NOTIFICATION_VALUE')


def instantiate_environment():
    if environment["update_interval"] == '':
        raise ValueError("Missing `update_interval`")

    if environment["currency"] == '':
        raise ValueError("Missing `currency`.")

    if environment["cryptos"] == '':
        raise ValueError("Missing `cryptos`.")
    else:
        environment["cryptos"] = environment["cryptos"].split(",")

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

    if environment["sell_notification_value"] == '':
        raise ValueError("Missing `sell_notification_value`.")
    else:
        environment["sell_notification_value"] = environment["sell_notification_value"].split(",")

    if environment["buy_notification_value"] == '':
        raise ValueError("Missing `buy_notification_value`.")
    else:
        environment["buy_notification_value"] = environment["buy_notification_value"].split(",")

    return environment
