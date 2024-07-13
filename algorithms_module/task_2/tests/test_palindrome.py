import pytest
from algorithms_module.task_2.src.palindrome import palindrome

@pytest.mark.parametrize('value, expected_result',
                         [
                             (12321, True),
                             (121, True),
                             (1, True),
                             (1223, False)
                         ])

def test_palindrome_positive(value, expected_result):
    assert palindrome(value) == expected_result

@pytest.mark.parametrize('value, expected_result',
                         [
                             (None, pytest.raises(TypeError)),
                             ('1', pytest.raises(TypeError)),
                             (1.0, pytest.raises(TypeError))
                         ])

def test_palindrome_negative(value, expected_result):

    with expected_result:
        assert palindrome(value) == expected_result