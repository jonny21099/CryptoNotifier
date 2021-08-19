import dotenv
import os

dotenv.load_dotenv()

update_interval = os.getenv("UPDATE_INTERVAL")

coinbase_api_key = os.getenv('COINBASE_API_KEY')
coinbase_secret_key = os.getenv('COINBASE_SECRET_KEY')

currency = os.getenv('CURRENCY')
cryptos = os.getenv('CRYPTOS')

email_sender = os.getenv('EMAIL_SENDER')
email_sender_password = os.getenv('EMAIL_SENDER_PASSWORD')
email_receiver = os.getenv('EMAIL_RECEIVER')
smtp_server = os.getenv('SMTP_SERVER')

sell_notification_value = os.getenv('SELL_NOTIFICATION_VALUE')
buy_notification_value = os.getenv('BUY_NOTIFICATION_VALUE')


def instantiate_environment():
    global update_interval, currency, cryptos, email_sender, email_receiver, email_sender_password, smtp_server, \
        sell_notification_value, buy_notification_value

    if update_interval == '':
        raise ValueError("Missing `update_interval`")

    if currency == '':
        raise ValueError("Missing `currency`.")

    if cryptos == '':
        raise ValueError("Missing `cryptos`.")
    else:
        cryptos = cryptos.split(",")

    if email_sender == '':
        raise ValueError("Missing `email_sender`.")

    if email_receiver == '':
        raise ValueError("Missing `email_receiver`.")
    else:
        email_receiver = email_receiver.split(",")

    if email_sender_password == '':
        raise ValueError("Missing `email_sender_password`.")

    if smtp_server == '':
        raise ValueError("Missing `smtp_server`.")

    if sell_notification_value == '':
        raise ValueError("Missing `sell_notification_value`.")
    else:
        sell_notification_value = sell_notification_value.split(",")

    if buy_notification_value == '':
        raise ValueError("Missing `buy_notification_value`.")
    else:
        buy_notification_value = buy_notification_value.split(",")

    return update_interval, coinbase_api_key, coinbase_secret_key, currency, cryptos, email_sender, \
           email_sender_password, email_receiver, smtp_server, sell_notification_value, buy_notification_value
