from algorithms_module.task_4.src.sum_of_digits import sum_of_digits
import pytest

@pytest.mark.parametrize('n, expected_result',
                         [
                             (123, 6),
                             (516, 12),
                             (0, 0),
                             (1, 1)
                         ])

def test_sum_of_digits_positive(n, expected_result):
    assert sum_of_digits(n) == expected_result
