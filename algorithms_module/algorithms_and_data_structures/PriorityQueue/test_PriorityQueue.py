import pytest
from algorithms_module.algorithms_and_data_structures.PriorityQueue.PriorityQueue import PriorityQueue

@pytest.mark.parametrize('initial_data, item, priority, expected_result',
                         [
                             ([(3, 'low'), (1, 'high')], 'medium', 2, ['high', 'medium', 'low']),
                             ([], 'high', 1, ['high'])
                         ])

def test_enqueue(initial_data, item, priority, expected_result):
    pq = PriorityQueue()
    for p, i in initial_data:
        pq.enqueue(i, p)

    pq.enqueue(item, priority)

    result = []
    while not pq.is_empty():
        result.append(pq.dequeue())
    assert result == expected_result

@pytest.mark.parametrize('initial_data, expected_result',
                         [
                             ([(1, 'high'), (2, 'medium'), (3, 'low')], ['high', 'medium', 'low']),
                             ([(2, 'medium'), (1, 'high')], ['high', 'medium']),
                         ])

def test_dequeue(initial_data, expected_result):
    pq = PriorityQueue()
    for p, i in initial_data:
        pq.enqueue(i,p)

    result = []
    while not pq.is_empty():
        result.append(pq.dequeue())

    assert result == expected_result

@pytest.mark.parametrize('initial_data, expected_result',
                         [
                             ([(1, 'high'), (2, 'medium'), (3, 'low')], 'high'),
                             ([(1, 'medium'), (2, 'low')], 'medium'),
                         ])

def test_peek(initial_data, expected_result):
    pq = PriorityQueue()
    for p, i in initial_data:
        pq.enqueue(i, p)

    assert pq.peek() == expected_result
