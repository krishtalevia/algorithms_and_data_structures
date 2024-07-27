import pytest
from algorithms_module.task_4.src.is_palindrome import is_palindrome

@pytest.mark.parametrize('text, expected_result',
                         [
                             ('123', False),
                             ('121', True),
                             ('1', True),
                             ('', True)
                         ])

def test_is_palindrome_positive(text, expected_result):
    assert is_palindrome(text) == expected_result