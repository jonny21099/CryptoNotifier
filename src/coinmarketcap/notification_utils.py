class NotificationUtils:
    @staticmethod
    def compare_price(current_price, sell_notification_value, buy_notification_value, crypto):
        if float(current_price) >= float(sell_notification_value):
            print(f"The price of {crypto} has reached {current_price}.")
            buy = False
        elif float(current_price) <= float(buy_notification_value):
            print(f"The price of {crypto} has dropped to {current_price}.")
            buy = True
        else:
            buy = None
        return buy
