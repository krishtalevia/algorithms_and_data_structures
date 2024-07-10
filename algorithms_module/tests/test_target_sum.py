import pytest
from algorithms_module.src.task_3 import target_sum

@pytest.mark.parametrize('list, target, expected_result',
                         [
                             ([2, 7, 11, 15], 9, [0,1]),
                             ([3, 2, 4], 6, [1,2])
                         ])

def test_target_sum_positive(list, target, expected_result):
    assert target_sum(list, target) == expected_result

@pytest.mark.parametrize('list, target, expected_result',
                         [
                             (['2, 4, 6, 8, 10'], 1, pytest.raises(Exception)),
                             ([''], '', pytest.raises(Exception)),
                             ([1.0, 1.0, None], 2.0, pytest.raises(Exception))
                         ])

def test_target_sum_negative(list, target, expected_result):
    with expected_result:
        assert target_sum(list, target) == expected_result