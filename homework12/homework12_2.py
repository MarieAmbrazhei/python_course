"""Homework12_2: OOP. Writing and implementing programs."""


# Task_2 Bank.

class Deposit:
    """ A class to represent a deposit."""

    def __init__(self, amount, term):
        """Initializes the Deposit object with an amount and term"""
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


bank_1 = Bank(10)
dep_1 = Deposit(10000, 2)
dep_2 = Deposit(15000, 2)
assert bank_1.deposit(dep_1) == 12203.909613755592
assert bank_1.deposit(dep_2) == 18305.86442063339
