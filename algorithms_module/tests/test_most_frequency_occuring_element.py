import pytest
from algorithms_module.src.task_2 import most_frequency_occuring_element

@pytest.mark.parametrize('list, expected_result',
                         [
                             ([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 4),
                             ([7], 7),
                             ([1, 2, 3, 4, 5], 1)
                         ])

def test_most_frequency_occuring_element_positive(list, expected_result):
    assert most_frequency_occuring_element(list) == expected_result

@pytest.mark.parametrize('list, expected_result',
                         [
                             (['2, 4, 6, 8, 10'], pytest.raises(Exception)),
                             ([''], pytest.raises(Exception)),
                             ([1.0, None], pytest.raises(Exception))
                         ])

def test_most_frequency_occuring_element_negative(list, expected_result):
    with expected_result:
        assert most_frequency_occuring_element(list) == expected_result