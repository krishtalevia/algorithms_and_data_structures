from classwork_2.src.average import average
import pytest

@pytest.mark.parametrize('value, expected_result',
                         [
                             ([1], 1),
                             ([-1], -1),
                             ([1, 2, 3], 2),
                             ([5, 15, 25, 35], 20),
                             ([-1, -2, -3], -2),
                             ([-10, -20, -30], -20),
                             ([0, 0, 0], 0),
                             ([0, -1, -2], -1),
                             ([0.5, 1.5, 2.5], 1.5),
                             ([2, 2, 2, 2, 2], 2),
                             ([10, -10, 20, -20, 30, -30], 0),
                             ([10, 20, -20, 30, -30], 2),
                             ([1, 2.5, 3.75, 4.25], 2.875),
                             ([10, 10, 100, 10, 100000], 20026),
                             ([1000000, 1, 1, 1, 1], 200000.8)
                         ])

def test_average_positive(value, expected_result):
    assert average(value) == expected_result

@pytest.mark.parametrize('value, expected_result',
                         [
                             ([], pytest.raises(ValueError)),
                             ([None, 2, True], pytest.raises(TypeError))
                         ])

def test_average_negative(value, expected_result):
    with expected_result:
        assert average(value) == expected_result
