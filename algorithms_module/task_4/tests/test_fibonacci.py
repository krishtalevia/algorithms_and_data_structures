from algorithms_module.task_4.src.fibonacci import fibonacci
import pytest

@pytest.mark.parametrize('n, expected_result',
                         [
                             (5, 5),
                             (10, 55)
                         ])

def test_fibonacci_positive(n, expected_result):
    assert fibonacci(n) == expected_result
