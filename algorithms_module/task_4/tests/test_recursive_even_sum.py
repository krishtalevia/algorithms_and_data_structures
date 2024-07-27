from algorithms_module.task_4.src.recursive_even_sum import recursive_even_sum
import pytest

@pytest.mark.parametrize('lst, expected_result',
                         [
                             ([1, 2, 3, 4], 6),
                             ([1, 2, 3], 2)
                         ])

def test_recursive_even_sum_positive(lst, expected_result):
    assert recursive_even_sum(lst) == expected_result
