import pytest
from algorithms_module.task_3.src.reverse_even_elements import reverse_even_elements

@pytest.mark.parametrize('lst, expected_result',
                         [
                             ([1, 2, 3, 4, 5, 6], [1, 6, 3, 4, 5, 2]),
                             ([1, 2, 3, 4], [1, 4, 3, 2]),
                             ([], []),
                             ([2], [2])
                         ])

def test_reverse_even_elements_positive(lst, expected_result):
    assert reverse_even_elements(lst) == expected_result

@pytest.mark.parametrize('lst, expected_result',
                         [
                             (None, pytest.raises(TypeError)),
                             ([1, '2', 3], pytest.raises(TypeError))
                         ])

def test_reverse_even_elements_negative(lst, expected_result):

    with expected_result:
        assert reverse_even_elements(lst) == expected_result