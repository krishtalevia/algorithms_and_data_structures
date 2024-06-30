from classwork_1.src.calculator import Calculator

import pytest

calc = Calculator()

@pytest.mark.parametrize('value1, value2, expected_result',
                         [
                             (1, 2, 3),
                             (10, 100, 110),
                             (50, 50, 100),
                             (-1, -2, -3),
                             (-1, 2, 1),
                             (0, 0, 0),
                             (-1, 0, -1),
                             (1, 0, 1)
                         ])

def test_add_positive(value1, value2, expected_result):
    global calc

    assert calc.add(value1, value2) == expected_result

@pytest.mark.parametrize('value1, value2, expected_result',
                         [
                             ('1', 2, pytest.raises(TypeError)),
                             (None, 2, pytest.raises(TypeError)),
                             (True, 2, pytest.raises(AssertionError)),
                             (True, False, pytest.raises(AssertionError)),
                             ('str', 'str', pytest.raises(AssertionError))
                         ])

def test_add_negative(value1, value2, expected_result):
    global calc

    with expected_result:
        assert calc.add(value1, value2) == expected_result

@pytest.mark.parametrize('value1, value2, expected_result',
                         [
                             (1, 2, -1),
                             (10, 100, -90),
                             (50, 50, 0),
                             (-1, -2, 1),
                             (-1, 2, -3),
                             (0, 0, 0),
                             (1, 0, 1),
                             (-1, 0, -1)
                         ])

def test_subtract_positive(value1, value2, expected_result):
    global calc

    assert calc.subtract(value1, value2) == expected_result

@pytest.mark.parametrize('value1, value2, expected_result',
                         [
                             ('1', 1, pytest.raises(TypeError))
                         ])

def test_subtract_negative(value1, value2, expected_result):
    global calc

    with expected_result:
        assert calc.subtract(value1, value2) == expected_result

@pytest.mark.parametrize('value1, value2, expected_result',
                         [
                             (1, 2, 2),
                             (10, 100, 1000),
                             (50, 50, 2500),
                             (-1, -2, 2),
                             (-1, 2, -2),
                             (0, 0, 0),
                             (1, 0, 0),
                             (-1, 0, 0)
                         ])

def test_multiply_positive(value1, value2, expected_result):
    global calc

    assert calc.multiply(value1, value2) == expected_result

@pytest.mark.parametrize('value1, value2, expected_result',
                         [
                             ('1', 1, pytest.raises(TypeError))
                         ])

def test_multiply_negative(value1, value2, expected_result):
    global calc

    with expected_result:
        assert calc.multiply(value1, value2) == expected_result

@pytest.mark.parametrize('value1, value2, expected_result',
                         [
                             (1, 2, 0.5),
                             (100, 10, 10),
                             (50, 50, 1),
                             (-1, -2, 0.5),
                             (-1, 1, -1),
                         ])

def test_divide_positive(value1, value2, expected_result):
    global calc

    assert calc.divide(value1, value2) == expected_result

@pytest.mark.parametrize('value1, value2, expected_result',
                         [
                             (1, 0, pytest.raises(ZeroDivisionError)),
                             (0, 0, pytest.raises(ZeroDivisionError)),
                             ("1", 2, pytest.raises(TypeError))
                         ])

def test_divide_negative(value1, value2, expected_result):
    global calc

    with expected_result:
        assert calc.divide(value1, value2) == expected_result