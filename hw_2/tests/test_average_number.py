import pytest
from hw_2.src.average_number import average


@pytest.mark.parametrize('value, expected_result',
                         [
                             ([1, 2, 3], 2.0),
                             ([-1, -2, -3], -2.0),
                             ([-1, 2, -3], -0.7),
                             ([0, 0, 0], 0.0),
                             ([1, 0, 3], 1.3),
                             ([-1, 0, -3], -1.3),
                             ([1, 1, 1], 1.0),
                             ([3, 2, 1], 2.0),
                             ([1, 2, 3], 2.0),
                             ([1, 100000, 2, 100000000], 25025000.8),
                             ([1.0, 2.5, 3.9], 2.5),
                             ([1, 2, 3], 2.0),
                             ([1, 2.5, 3], 2.2),
                             ([1], 1.0),
                             ([i for i in range(1, 1001)], 500.5)
                         ])

def test_average_positive(value, expected_result):
    assert average(value) == expected_result

@pytest.mark.parametrize('value, expected_result',
                         [
                             (['a', 'b', 'c'], pytest.raises(TypeError)),
                             (['1', '2', '3'], pytest.raises(TypeError)),
                             (['?', '-', '_'], pytest.raises(TypeError)),
                             ([1, '-', '_'], pytest.raises(TypeError)),
                             ([1, '2', 3.0], pytest.raises(TypeError)),
                             ([], pytest.raises(ValueError))
                         ])

def test_average_negative(value, expected_result):

    with expected_result:
        assert average(value) == expected_result