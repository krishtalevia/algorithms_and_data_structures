import pytest
from algorithms_module.algorithms_and_data_structures.Stack.Stack import Stack

@pytest.mark.parametrize('initiail_data, item, expected_result',
                         [
                             ([1, 2, 3], 4, [1, 2, 3, 4]),
                             ([], 1, [1])
                         ])

def test_push(initiail_data, item, expected_result):
    s = Stack()
    for i in initiail_data:
        s.push(i)

    s.push(item)

    result = []
    while not s.is_empty():
        result.append(s.pop())

    result.reverse()

    assert result == expected_result
@pytest.mark.parametrize('initial_data, expected_result',
                         [
                             ([1, 2, 3], 3),
                             ([], None)
                         ])

def test_peek(initial_data, expected_result):
    s = Stack()
    for i in initial_data:
        s.push(i)

    assert s.peek() == expected_result

@pytest.mark.parametrize('initial_data, expected_result',
                         [
                             ([1, 2, 3], 3),
                             ([], None)
                         ])

def test_pop(initial_data, expected_result):
    s = Stack()
    for i in initial_data:
        s.push(i)

    assert s.pop() == expected_result

@pytest.mark.parametrize('initial_data, expected_result',
                         [
                             ([1, 2, 3], False),
                             ([], True)
                         ])

def test_peek(initial_data, expected_result):
    s = Stack()
    for i in initial_data:
        s.push(i)

    assert s.is_empty() == expected_result