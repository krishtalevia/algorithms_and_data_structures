from algorithms_module.task_4.src.recursive_sum import recursive_sum
import pytest

@pytest.mark.parametrize('lst, expected_result',
                         [
                             ([3, 2, 1], 6),
                             ([1, 2, 3, 4], 10)
                         ])

def test_recursive_sum_positive(lst, expected_result):
    assert recursive_sum(lst) == expected_result
