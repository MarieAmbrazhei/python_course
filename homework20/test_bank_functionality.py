"""
Unit tests for the Homework_12: bank.
"""

import unittest
from homework12.homework12_2 import Bank, Deposit
from pymar_logger import logger as log


class TestBank(unittest.TestCase):
    """
    Test cases for the Bank class deposit method.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.bank_1 = Bank(10)
        self.dep_1 = Deposit(10000, 2)
        self.dep_2 = Deposit(15000, 2)

    def tearDown(self):
        """
        Clean up after each test.
        """
        del self.bank_1
        del self.dep_1
        del self.dep_2

    def test_deposit_1(self):
        """
        Test deposit method with dep_1.
        """
        expected_amount = 12203.909613755592
        result = self.bank_1.deposit(self.dep_1)
        log.info(f'Testing depo_1: expected {expected_amount}, got {result}')
        self.assertAlmostEqual(result, expected_amount, places=2)

    def test_deposit_2(self):
        """
        Test deposit method with dep_2.
        """
        expected_amount = 18305.86442063339
        result = self.bank_1.deposit(self.dep_2)
        log.info(f'Testing depo_2: expected {expected_amount}, got {result}')
        self.assertAlmostEqual(result, expected_amount, places=2)

    def test_is_instance(self):
        """
        Test if dep_1 is an instance of Deposit.
        """
        self.assertIsInstance(self.dep_1, Deposit)
        log.info('Testing dep_1 is an instance of Deposit')

    def test_deposit_total_sum(self):
        """
        Test that the deposit amount is greater than the initial amount.
        """
        self.assertGreater(self.bank_1.deposit(self.dep_1), self.dep_1.amount)
        log.info('Testing total sum: deposit amount is greater than'
                 ' initial amount')

    def test_deposit_is_true(self):
        """
        Test that the deposit amount is truthy value.
        """
        self.assertTrue(self.bank_1.deposit(self.dep_1))
        log.info('Testing deposit is true')

    def test_deposit_amount_less(self):
        """
        Test that the deposit amount is less than the bank's deposit result.
        """
        self.assertLess(self.dep_1.amount, self.bank_1.deposit(self.dep_1))
        log.info(
            f'Testing deposit amount: {self.dep_1.amount} is less than bank'
            f's deposit result')


if __name__ == '__main__':
    unittest.main()
