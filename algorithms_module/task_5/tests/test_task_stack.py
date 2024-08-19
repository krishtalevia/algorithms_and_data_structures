import pytest
from algorithms_module.task_5.src.project_task import *

@pytest.mark.parametrize('initiail_data, item, expected_result',
                         [
                             ([1, 2, 3], 4, [1, 2, 3, 4]),
                             ([], 1, [1])
                         ])

def test_push(initiail_data, item, expected_result):
    ts = TaskStack()
    for i in initiail_data:
        ts.push(i)

    ts.push(item)

    result = []
    while not ts.is_empty():
        result.append(ts.pop())

    result.reverse()

    assert result == expected_result
@pytest.mark.parametrize('initial_data, expected_result',
                         [
                             ([1, 2, 3], 3),
                             ([], None)
                         ])

def test_peek(initial_data, expected_result):
    ts = TaskStack()
    for i in initial_data:
        ts.push(i)

    assert ts.peek() == expected_result

@pytest.mark.parametrize('initial_data, expected_result',
                         [
                             ([1, 2, 3], 3),
                             ([], None)
                         ])

def test_pop(initial_data, expected_result):
    ts = TaskStack()
    for i in initial_data:
        ts.push(i)

    assert ts.pop() == expected_result

@pytest.mark.parametrize('initial_data, expected_result',
                         [
                             ([1, 2, 3], False),
                             ([], True)
                         ])

def test_peek(initial_data, expected_result):
    ts = TaskStack()
    for i in initial_data:
        ts.push(i)

    assert ts.is_empty() == expected_result