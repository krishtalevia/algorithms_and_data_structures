import pytest
from hw_2.src.factorial import factorial
import math


@pytest.mark.parametrize('value, expected_result',
                         [
                             (1, 1),
                             (2, 2),
                             (3, 6),
                             (4, 24),
                             (5, 120),
                             (10, 3628800),
                             (15, 1307674368000),
                             (20, math.factorial(20)),
                             (50, math.factorial(50)),
                             (0, 1),
                             (100, math.factorial(100)),
                             (5, 120)
                         ])

def test_factorial_positive(value, expected_result):
    assert factorial(value) == expected_result

@pytest.mark.parametrize('value, expected_result',
                         [
                             (5.0, pytest.raises(TypeError)),
                             (-5, pytest.raises(ValueError)),
                             (-10, pytest.raises(ValueError)),
                             (-5.0, pytest.raises(ValueError)),
                             (None, pytest.raises(TypeError)),
                             (True, pytest.raises(AssertionError)),
                             ([5], pytest.raises(TypeError)),
                             (5.0, pytest.raises(TypeError))
                         ])

def test_average_negative(value, expected_result):

    with expected_result:
        assert factorial(value) == expected_result