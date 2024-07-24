"""Homework21_1: test_bank_functionality"""
import pytest

from homework12.homework12_2 import Deposit
from pymar_logging import logger as log


@pytest.mark.parametrize('dep, expected_amount',
                         [(Deposit(10000, 2), 12203.90961375559),
                          (Deposit(15000, 2),
                           18305.86442063339)])
def test_deposit(initial_bank, dep, expected_amount):
    """
    Test deposit method with dep_2.
    """
    bank_1 = initial_bank
    result = bank_1.deposit(dep)
    log.info(f'Testing deposit: expected {expected_amount}, got {result}')
    assert round(result, 2) == round(expected_amount, 2), (
        f'Result {result} does not match the expected amount {expected_amount}'
    )
    log.info('Successfully verified deposit calculation')


def test_is_instance(deposit_1):
    """
    Test if dep_1 is an instance of Deposit.
    """
    dep_1 = deposit_1
    log.info('Starting homework21 to verify if dep_1 is an instance of '
             'Deposit.')
    assert isinstance(dep_1, Deposit), (
        f'dep_1 is not an instance of Deposit. Actual type: {type(dep_1)}'
    )
    log.info('Testing dep_1 is an instance of Deposit')
    log.info('Successfully verified dep_1 is an instance of Deposit')


def test_deposit_total_sum(initial_bank, deposit_1):
    """
    Test that the deposit amount is greater than the initial amount.
    """
    bank_1 = initial_bank
    dep_1 = deposit_1
    result = bank_1.deposit(dep_1)
    log.info(
        'Starting homework21 to verify that the deposit amount is greater'
        ' than the initial amount.')
    assert bank_1.deposit(dep_1) > dep_1.amount, (
        f'Deposit result {result} should be greater than the initial amount '
        f'{dep_1.amount}.'
    )
    log.info('Testing total sum: deposit amount is greater than'
             ' initial amount')
    log.info(
        f'Successfully verified that the deposit result {result} is '
        f'greater than the initial amount {dep_1.amount}.')


def test_deposit_is_true(initial_bank, deposit_1):
    """
    Tet that the deposit amount is truthy value.
    """
    bank_1 = initial_bank
    dep_1 = deposit_1

    log.info(
        'Starting homework21 to verify that deposit method returns a'
        ' truthy value.'
    )
    assert bank_1.deposit(dep_1), (
        'Deposit method did not return a truthy value.'
    )
    log.info('Testing deposit is true')
    log.info(
        'Successfully verified that deposit method returns a truthy value.')


def test_deposit_amount_less(initial_bank, deposit_1):
    """
    Test that the deposit amount is less than the bank's deposit result.
    """
    bank_1 = initial_bank
    dep_1 = deposit_1
    deposit_result = bank_1.deposit(dep_1)
    log.info(
        'Starting homework21 to verify that deposit amount is less than the '
        'bank\'s deposit result.')
    assert dep_1.amount < deposit_result, (
        f'Deposit amount {dep_1.amount} is not less than the bank\'s '
        f'deposit result {deposit_result}.'
    )
    log.info(
        f'Testing deposit amount: {dep_1.amount} is less than bank'
        f's deposit result')
    log.info(
        f'Successfully verified that deposit amount {dep_1.amount} is '
        f'less than the bank\'s deposit result {deposit_result}.'
    )
