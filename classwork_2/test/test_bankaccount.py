from classwork_2.src.bankaccount import BankAccount
import pytest

bank_account = BankAccount()
bank_account.deposit(1000)


@pytest.mark.parametrize('amount, expected_result',
                         [
                             (10, 1010),
                             (194, 1194),
                             (100000, 101000)
                         ])

def test_bank_account_deposit_positive(amount, expected_result):
    bank_account.deposit(amount)

    assert bank_account.get_balance() == expected_result
    bank_account.withdraw(amount)