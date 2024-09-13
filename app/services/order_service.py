from models.order_models import Order
from config.config import OrderConfig


class OrderService:
    def process_order(self, order: Order):
        if not self._name_check_english(order.name):
            raise ValueError("Name contains non-English characters")
        if not self._name_check_capital(order.name):
            raise ValueError("Name is not capitalized")
        if not self._is_valid_currency(order.currency):
            raise ValueError("Currency format is wrong")
        order = self._usd2twd(order)
        if not self._is_valid_price(order.price):
            raise ValueError(f"Price is over {OrderConfig.price_quota}")
        if not self._is_positive_price(order.price):
            raise ValueError("Can not accept negative price")

        return order.__dict__

    def _name_check_english(self, name: str) -> bool:
        name_list = name.split()
        for name_string in name_list:
            if str.isalpha(name_string) is False:
                return False
        return True

    def _name_check_capital(self, name: str) -> bool:
        name_list = name.split()
        for name_string in name_list:
            if str.istitle(name_string) is False:
                return False
        return True

    def _is_valid_currency(self, currency: str) -> bool:
        valid_currencies = OrderConfig.valid_currencies
        return currency in valid_currencies

    def _usd2twd(self, order: Order):
        if order.currency == "USD":
            order.currency = "TWD"
            order.price = order.price * OrderConfig.usd2twd_exchange_rate
        return order

    def _is_valid_price(self, price: float) -> bool:
        return price <= OrderConfig.price_quota

    def _is_positive_price(self, price: float) -> bool:
        return price > 0
