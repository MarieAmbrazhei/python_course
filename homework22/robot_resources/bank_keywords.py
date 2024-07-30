from robot.api.deco import keyword
from homework12.homework12_2 import Bank, Deposit
from pymar_log import logger as log


@keyword
def create_bank(percent):
    """
    Creates a new Bank instance with a specified interest rate.
    """
    return Bank(float(percent))


@keyword
def create_deposit(amount, term):
    """
    Creates a new Deposit instance with a specified amount and term.
    """
    return Deposit(float(amount), int(term))


@keyword
def deposit_money(bank, deposit):
    """
    Deposits money into a bank using a Deposit instance.
    """
    return bank.deposit(deposit)


@keyword
def log_message(message):
    """
    Logs a message using the logging system.
    """
    log.info(message)


@keyword
def check_if_instance(obj):
    """
    Checks if the given object is an instance of the Deposit class.
    """
    return isinstance(obj, Deposit)
