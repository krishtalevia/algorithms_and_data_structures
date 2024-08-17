import pytest
from algorithms_module.algorithms_and_data_structures.DeQueue.DeQueue import DeQueue

@pytest.mark.parametrize('elements, expected_result',
                         [
                             ([], True),
                             ([1], False)
                         ])

def test_is_empty(elements, expected_result):
    dq = DeQueue()
    for i in elements:
        dq.add_rear(i)
    assert dq.is_empty() == expected_result

@pytest.mark.parametrize('elements, add_el, expected_result',
                         [
                             ([1, 2, 3], 4, [1, 2, 3, 4]),
                             ([], 1, [1])
                         ])

def test_add_rear(elements, add_el, expected_result):
    dq = DeQueue()
    for i in elements:
        dq.add_rear(i)

    dq.add_rear(add_el)

    result = []
    while not dq.is_empty():
        result.append(dq.remove_front())

    assert result == expected_result

@pytest.mark.parametrize('elements, expected_result',
                         [
                             ([1, 2, 3], 1),
                             ([], None)
                         ])

def test_remove_front(elements, expected_result):
    dq = DeQueue()
    for i in elements:
        dq.add_rear(i)

    assert dq.remove_front() == expected_result

@pytest.mark.parametrize('elements, expected_result',
                         [
                             ([2, 3], 2),
                             ([4, 5], 4)
                         ])

def test_rear(elements, expected_result):
    dq = DeQueue()
    for i in elements:
        dq.add_rear(i)

    assert dq.peek_front() == expected_result