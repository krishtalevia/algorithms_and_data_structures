import pytest
from algorithms_module.task_3.src.large_integer import large_integer

@pytest.mark.parametrize('lst, expected_result',
                         [
                             ([3, 2, 1], [3, 2, 2]),
                             ([9, 9, 9], [1, 0, 0, 0]),
                             ([9], [1, 0]),
                             ([5, 4, 1], [5, 4, 2])
                         ])

def test_large_integer_positive(lst, expected_result):
    assert large_integer(lst) == expected_result

@pytest.mark.parametrize('lst, expected_result',
                         [
                             (None, pytest.raises(TypeError)),
                             ([1, '2', 3], pytest.raises(TypeError)),
                             ([10, 9, 8], pytest.raises(ValueError))
                         ])

def test_large_integer_negative(lst, expected_result):

    with expected_result:
        assert large_integer(lst) == expected_result