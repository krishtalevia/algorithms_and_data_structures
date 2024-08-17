import pytest
from algorithms_module.algorithms_and_data_structures.Queue.Queue import Queue

@pytest.mark.parametrize('elements, expected_result',
                         [
                             ([], True),
                             ([1], False)
                         ])

def test_is_empty(elements, expected_result):
    q = Queue()
    for i in elements:
        q.enqueue(i)
    assert q.is_empty() == expected_result

@pytest.mark.parametrize('elements, enqueue_el, expected_result',
                         [
                             ([1, 2, 3], 4, [1, 2, 3, 4]),
                             ([], 1, [1])
                         ])

def test_enqueue(elements, enqueue_el, expected_result):
    q = Queue()
    for i in elements:
        q.enqueue(i)
    q.enqueue(enqueue_el)

    result = []
    while not q.is_empty():
        result.append(q.dequeue())

    assert result == expected_result

@pytest.mark.parametrize('elements, expected_result',
                         [
                             ([1, 2, 3], 1),
                             ([], None)
                         ])

def test_dequeue(elements, expected_result):
    q = Queue()
    for i in elements:
        q.enqueue(i)

    assert q.dequeue() == expected_result

@pytest.mark.parametrize('elements, expected_result',
                         [
                             ([2, 3], 2),
                             ([4, 5], 4)
                         ])

def test_peek(elements, expected_result):
    q = Queue()
    for i in elements:
        q.enqueue(i)

    assert q.peek() == expected_result