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

@pytest.mark.parametrize('amount, expected_result',
                         [
                             (0, pytest.raises(ValueError)),
                             (-10, pytest.raises(ValueError))
                         ])

def test_bank_account_deposit_negative(amount, expected_result):
    with expected_result:
        assert bank_account.deposit(amount) == expected_result

@pytest.mark.parametrize('amount, expected_result',
                         [
                             (158, 842),
                             (1, 999),
                             (500, 500),
                             (1000, 0)
                         ])

def test_bank_account_withdraw_positive(amount, expected_result):
    bank_account.withdraw(amount)

    assert bank_account.get_balance() == expected_result
    bank_account.deposit(amount)
