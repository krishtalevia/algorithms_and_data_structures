import pytest
from algorithms_module.task_3.src.rotate_and_reverse import rotate_and_reverse

@pytest.mark.parametrize('lst, k, expected_result',
                         [
                             ([1, 2, 3, 4, 5, 6], 2, [5, 6, 1, 2, 3, 4]),
                             ([5, 4, 3, 2, 1], 1, [1, 5, 4, 3, 2])
                         ])

def test_rotate_and_reverse_positive(lst, k, expected_result):
    assert rotate_and_reverse(lst, k) == expected_result

@pytest.mark.parametrize('lst, k, expected_result',
                         [
                             (None, 1, pytest.raises(TypeError)),
                             ([1, '2', 3], 2, pytest.raises(TypeError))
                         ])

def test_rotate_and_reverse_negative(lst, k, expected_result):

    with expected_result:
        assert rotate_and_reverse(lst, k) == expected_result