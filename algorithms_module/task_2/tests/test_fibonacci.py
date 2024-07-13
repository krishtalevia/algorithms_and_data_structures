import pytest
from algorithms_module.task_2.src.fibonacci import fibonacci

@pytest.mark.parametrize('value, expected_result',
                         [
                             (1, [0, 1]),
                             (0, [0]),
                             (5, [0, 1, 1, 2, 3, 5])
                         ])

def test_fibonacci_positive(value, expected_result):
    assert fibonacci(value) == expected_result

@pytest.mark.parametrize('value, expected_result',
                         [
                             (None, pytest.raises(TypeError)),
                             (-1, pytest.raises(ValueError)),
                             ('5', pytest.raises(TypeError))
                         ])

def test_fibonacci_negative(value, expected_result):

    with expected_result:
        assert fibonacci(value) == expected_result