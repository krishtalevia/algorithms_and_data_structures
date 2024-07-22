import pytest
from algorithms_module.task_4.src.bubble_sort import bubble_sort

@pytest.mark.parametrize('array, expected_result',
                         [
                             ([3, 2, 1], [1, 2, 3]),
                             ([5, 3, 4, 2, 1], [1, 2, 3, 4, 5]),
                             ([1], [1]),
                             ([], [])
                         ])

def test_bubble_sort_positive(array, expected_result):
    assert bubble_sort(array) == expected_result