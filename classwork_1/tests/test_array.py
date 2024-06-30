from classwork_1.src.array import Array
import pytest


@pytest.mark.parametrize('args, expected_result',
                         [
                             ([1, 2, 3], 6),
                             ([-1, -2, -3], -6),
                             ([1, -2, 3], 2),
                             ([0, 1, -2], -1),
                             ([0, 0, 0], 0),
                             ([], 0),
                             ([1], 1),
                             ([1, 100, 100000], 100101),
                             ([10, 2, 5, -2, 1, -15], 1)
                         ])

def test_sum_positive(args, expected_result):
    array = Array(*args)
    assert array.sum() == expected_result

@pytest.mark.parametrize('args, expected_result',
                         [
                             (['1', 2, True], pytest.raises(TypeError))
                         ])

def test_sum_negative(args, expected_result):
    array = Array(*args)

    with expected_result:
        assert array.sum() == expected_result

@pytest.mark.parametrize('args, expected_result',
                         [
                             ([1, 2, 3], 6),
                             ([-1, -2, -3], -6),
                             ([1, -2, 3], -6),
                             ([0, 1, -2], 0),
                             ([0, 0, 0], 0),
                             ([], 1),
                             ([1], 1),
                             ([1, 100, 100000], 10000000),
                             ([10, 2, 5, -2, 1, -15], 3000)
                         ])

def test_multiply_positive(args, expected_result):
    array = Array(*args)
    assert array.multiply() == expected_result

@pytest.mark.parametrize('args, expected_result',
                         [
                             ([None, 2, True], pytest.raises(TypeError))
                         ])

def test_multiply_negative(args, expected_result):
    array = Array(*args)

    with expected_result:
        assert array.multiply() == expected_result

@pytest.mark.parametrize('args, expected_result',
                         [
                             ([1, 2, 3], 2),
                             ([-1, -2, -3], -2),
                             ([1, -2, 3], 0.6666666666666666),
                             ([0, 1, -2], -0.3333333333333333),
                             ([0, 0, 0], 0),
                             ([1], 1),
                             ([1, 100, 100000], 33367),
                             ([10, 2, 5, -2, 1, -15], 0.16666666666666666)
                         ])

def test_average_positive(args, expected_result):
    array = Array(*args)
    assert array.average() == expected_result

@pytest.mark.parametrize('args, expected_result',
                         [
                             ([], pytest.raises(ZeroDivisionError)),
                             ([None, 2, True], pytest.raises(TypeError))
                         ])

def test_multiply_negative(args, expected_result):
    array = Array(*args)

    with expected_result:
        assert array.average() == expected_result
