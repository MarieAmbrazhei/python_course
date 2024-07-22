"""Homework_13_2: OOP_2. Writing and implementing programs."""


# Task_2 Bank

class Deposit:
    """ A class to represent a deposit."""

    def __init__(self, amount, term):
        """Initializes the Deposit objects with an amount and term"""
        self.amount = amount
        self.term = term


class Bank:
    """ A class to represent a bank."""

    def __init__(self, percent):
        """Initializes the Bank object with an annual interest rate."""
        self.percent = percent

    def deposit(self, depo):
        """Calculates and prints the total amount after the term
        for a given deposit."""
        total = depo.amount * (1 + self.percent /
                               (100 * 12)) ** (12 * depo.term)
        return total

    @staticmethod
    def exchange_currency(from_currency, amount, to_currency='BYN'):
        """Converts the amount from one currency to another."""

        if from_currency == to_currency:
            return amount, to_currency

        exchange_rates = Currency.exchange_rates

        if (from_currency in exchange_rates
                and to_currency in exchange_rates[from_currency]):
            rate = (exchange_rates.get(from_currency, {})
                    .get(to_currency, 'Exchange rate not found '))
            if not isinstance(rate, float):
                return False
            converted_amount = round(amount * rate, 2)
            return converted_amount, to_currency

        raise ValueError(
            f"Exchange rate not available for {from_currency} to "
            f"{to_currency}")


class Currency:
    """This class is to store currencies rates"""
    exchange_rates = {
        'USD': {'BYN': 3.269, 'EUR': 0.929},
        'EUR': {'BYN': 7.04, 'USD': 2.152},
        'BYN': {'USD': 0.306, 'EUR': 0.142},
    }


class Person:
    """This class is to represent person with a
    specific currency and amount."""

    def __init__(self, currency, amount):
        """Initializes the Person objects."""
        self.currency = currency
        self.amount = amount


vasya = Person('USD', 10)
petya = Person('EUR', 5)
bank = Bank(10)
dep_1 = Deposit(10000, 2)
dep_2 = Deposit(15000, 2)
assert bank.deposit(dep_1) == 12203.909613755592
assert bank.deposit(dep_2) == 18305.86442063339
assert bank.exchange_currency(vasya.currency, vasya.amount) == (32.69, "BYN")
assert bank.exchange_currency(petya.currency, petya.amount) == (35.20, "BYN")
assert (bank.exchange_currency(vasya.currency, vasya.amount, 'EUR')
        == (9.29, "EUR"))
assert (bank.exchange_currency(petya.currency, petya.amount, 'USD')
        == (10.76, "USD"))
