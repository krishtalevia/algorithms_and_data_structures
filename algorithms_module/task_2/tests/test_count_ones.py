import pytest
from algorithms_module.task_2.src.count_ones import count_ones

@pytest.mark.parametrize('value, expected_result',
                         [
                             (1, 1),
                             (256, 1),
                             (523, 4)

                         ])

def test_count_ones_positive(value, expected_result):
    assert count_ones(value) == expected_result

@pytest.mark.parametrize('value, expected_result',
                         [
                             (None, pytest.raises(TypeError)),
                             (0, pytest.raises(ValueError)),
                             (-1, pytest.raises(ValueError))
                         ])

def test_count_ones_negative(value, expected_result):

    with expected_result:
        assert count_ones(value) == expected_result