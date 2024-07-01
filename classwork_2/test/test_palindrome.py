from classwork_2.src.palindrome import is_palindrome
import pytest

@pytest.mark.parametrize('value, expected_result',
                         [
                             ('тут', True),
                             ('тут как тут', True),
                             ('123321', True),
                             ('Тут как туТ', True),
                             ('!@# #@!', True),
                             ('!тут кАк тут!', True),
                             ('гром в молебен в небелом в морг', True),
                             ('Главрыба Дгвба гром в молебен — небелом в морг абвгД абырвалГ', True),
                             ('', True),
                             ('а', True)
                         ])

def test_is_palindrome_positive(value, expected_result):

    assert is_palindrome(value) == expected_result