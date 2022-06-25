import unittest

from exer7 import BankAccount


class TestBankAccount(unittest.TestCase):
    """
    Test Cases for the class BankAccount
    """

    def setUp(self):
        self.acct = BankAccount(name="Kobe", balance="10000")

    def test_case_withdraw(self):
        balance = 3000
        test_wd = self.acct.withdraw(balance)
        self.assertEquals(test_wd, 7000)

    def test_case_deposit(self):
        balance = 3000
        test_dep = self.acct.deposit(balance)
        self.assertEquals(test_dep, 13000)

if __name__ == '__main__':
    unittest.main()