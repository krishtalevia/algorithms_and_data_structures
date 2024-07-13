import pytest
from algorithms_module.task_2.src.factorial import factorial


@pytest.mark.parametrize('value, expected_result',
                         [
                             (1, 1),
                             (5, 120),
                             (8, 40320)

                         ])

def test_factorial_positive(value, expected_result):
    assert factorial(value) == expected_result

@pytest.mark.parametrize('value, expected_result',
                         [
                             (None, pytest.raises(TypeError)),
                             (0, pytest.raises(ValueError)),
                             (21, pytest.raises(ValueError))
                         ])

def test_factorials_negative(value, expected_result):

    with expected_result:
        assert factorial(value) == expected_result