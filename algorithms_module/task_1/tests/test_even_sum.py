import pytest
from algorithms_module.src.task_1 import even_sum

@pytest.mark.parametrize('list, expected_result',
                         [
                             ([2, 4, 6, 8, 10], 30),
                             ([-3, -4, -6, -8, -10], 1),
                             ([1, 2, 3, 4], 6)
                         ])

def test_even_sum_positive(list, expected_result):
    assert even_sum(list) == expected_result

@pytest.mark.parametrize('list, expected_result',
                         [
                             (['2, 4, 6, 8, 10'], pytest.raises(Exception)),
                             ([''], pytest.raises(Exception)),
                             ([1.0, None], pytest.raises(Exception))
                         ])

def test_even_sum_negative(list, expected_result):
    with expected_result:
        assert even_sum(list) == expected_result