from money import Money


class Bank:

    def __init__(self):
        self.exchange_rates = {}

    def add_exchange_rate(self, from_currency, to_currency, rate):
        key = from_currency + "->" + to_currency
        self.exchange_rates[key] = rate

    def convert(self, a_money, a_currency):
        if a_money.currency == a_currency:
            return Money(a_money.amount, a_currency), None

        key = a_money.currency + "->" + a_currency
        if key in self.exchange_rates:
            return Money(a_money.amount * self.exchange_rates[key], a_currency), None

        return None, key
