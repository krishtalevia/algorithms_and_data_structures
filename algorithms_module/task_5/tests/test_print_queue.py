import pytest
from algorithms_module.task_5.src.print_document import *

@pytest.mark.parametrize('elements, enqueue_el, expected_result',
                         [
                             ([1, 2, 3], 4, [1, 2, 3, 4]),
                             ([], 1, [1])
                         ])

def test_enqueue(elements, enqueue_el, expected_result):
    pq = PrintQueue()
    for i in elements:
        pq.enqueue(i)
    pq.enqueue(enqueue_el)

    result = []
    while not pq.is_empty():
        result.append(pq.dequeue())

    assert result == expected_result

@pytest.mark.parametrize('elements, expected_result',
                         [
                             ([1, 2, 3], 1),
                             ([], None)
                         ])

def test_dequeue(elements, expected_result):
    pq = PrintQueue()
    for i in elements:
        pq.enqueue(i)

    assert pq.dequeue() == expected_result

@pytest.mark.parametrize('elements, expected_result',
                         [
                             ([2, 3], 2),
                             ([4, 5], 4)
                         ])

def test_peek(elements, expected_result):
    pq = PrintQueue()
    for i in elements:
        pq.enqueue(i)

    assert pq.peek() == expected_result