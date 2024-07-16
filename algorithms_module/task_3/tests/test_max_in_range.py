import pytest
from algorithms_module.task_3.src.max_in_range import max_in_range

@pytest.mark.parametrize('lst, start, end, expected_result',
                         [
                             ([1, 2, 3, 4, 5], 1, 3, [4, 3, 2]),
                             ([5, 4, 3, 2, 1], 0, 4, [5, 0, 0])
                         ])

def test_max_in_range_positive(lst, start, end, expected_result):
    assert max_in_range(lst, start, end) == expected_result

@pytest.mark.parametrize('lst, start, end, expected_result',
                         [
                             (None, 0, 3, pytest.raises(TypeError)),
                             ([1, '2', 3], 0, 3, pytest.raises(TypeError)),
                             ([1, 2, 3, 4, 5], -1, 4, pytest.raises(ValueError))
                         ])

def test_max_in_range_negative(lst, start, end, expected_result):

    with expected_result:
        assert max_in_range(lst, start, end) == expected_result