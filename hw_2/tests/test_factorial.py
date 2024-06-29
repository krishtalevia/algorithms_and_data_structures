import pytest
from hw_2.src.factorial import factorial


@pytest.mark.parametrize('value, expected_result',
                         [
                             (5, 120),
                             (0, 1),
                             (100, 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000),
                             (5, 120)
                         ])

def test_factorial_positive(value, expected_result):
    assert factorial(value) == expected_result

@pytest.mark.parametrize('value, expected_result',
                         [
                             (5.0, pytest.raises(TypeError)),
                             (-5, pytest.raises(ValueError)),
                             (-5.0, pytest.raises(ValueError)),
                             (None, pytest.raises(TypeError)),
                             (True, pytest.raises(AssertionError)),
                             ([5], pytest.raises(TypeError))
                         ])

def test_average_negative(value, expected_result):

    with expected_result:
        assert factorial(value) == expected_result