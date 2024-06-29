from classwork_1.src.calculator import Calculator

import pytest

calc = Calculator()

@pytest.mark.parametrize('value1, value2, expected_result',
                         [
                             (5, 5, 10),
                             (-5, -5, -10),
                             (5, 50000, 50005),
                             (5, 0, 5)
                         ])

def test_add_positive(value1, value2, expected_result):
    global calc

    assert calc.add(value1, value2) == expected_result

@pytest.mark.parametrize('value1, value2, expected_result',
                         [
                             ('5', '5', pytest.raises(AssertionError))
                         ])

def test_add_negative(value1, value2, expected_result):
    global calc

    with expected_result:
        assert calc.add(value1, value2) == expected_result

@pytest.mark.parametrize('value1, value2, expected_result',
                         [
                             (5, 5, 0),
                             (-5, -5, 0),
                             (5, 50000, -49995),
                             (5, 0, 5)
                         ])

def test_subtract_positive(value1, value2, expected_result):
    global calc

    assert calc.subtract(value1, value2) == expected_result

@pytest.mark.parametrize('value1, value2, expected_result',
                         [
                             ('5', '5', pytest.raises(TypeError))
                         ])

def test_subtract_negative(value1, value2, expected_result):
    global calc

    with expected_result:
        assert calc.subtract(value1, value2) == expected_result

@pytest.mark.parametrize('value1, value2, expected_result',
                         [
                             (5, 5, 25),
                             (-5, -5, 25),
                             (5, 50000, 250000),
                             (5, 0, 0)
                         ])

def test_multiply_positive(value1, value2, expected_result):
    global calc

    assert calc.multiply(value1, value2) == expected_result

@pytest.mark.parametrize('value1, value2, expected_result',
                         [
                             ('5', '5', pytest.raises(TypeError))
                         ])

def test_multiply_negative(value1, value2, expected_result):
    global calc

    with expected_result:
        assert calc.multiply(value1, value2) == expected_result

@pytest.mark.parametrize('value1, value2, expected_result',
                         [
                             (5, 5, 1),
                             (-5, -5, 1),
                             (5, 50000, 0.0001)
                         ])

def test_divide_positive(value1, value2, expected_result):
    global calc

    assert calc.divide(value1, value2) == expected_result

@pytest.mark.parametrize('value1, value2, expected_result',
                         [
                             ('5', '5', pytest.raises(TypeError)),
                             (5, 0, pytest.raises(ZeroDivisionError))
                         ])

def test_multiply_negative(value1, value2, expected_result):
    global calc

    with expected_result:
        assert calc.divide(value1, value2) == expected_result