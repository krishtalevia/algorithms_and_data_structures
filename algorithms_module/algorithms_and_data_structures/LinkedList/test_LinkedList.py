import pytest
from algorithms_module.algorithms_and_data_structures.LinkedList.LinkedList import LinkedList

@pytest.mark.parametrize('elements, expected_result',
                         [
                             ([1, 2, 3], False),
                             ([], True)
                         ])

def test_is_empty(elements, expected_result):
    ll = LinkedList()
    for i in elements:
        ll.add_back(i)
    assert ll.is_empty() == expected_result

@pytest.mark.parametrize('elements, expected_result',
                         [
                             ([1, 2, 3], [1, 2, 3, 4]),
                             ([], [1])
                         ])

def test_add_back(elements, expected_result):
    ll = LinkedList()
    for i in elements:
        ll.add_back(i)
    ll.add_back(expected_result[-1])

    result = []
    iterator = ll.get_head()
    while iterator is not None:
        result.append(iterator.data)
        iterator = iterator.next

    assert result == expected_result

@pytest.mark.parametrize('elements, expected_result',
                         [
                             ([1, 2, 3], [0, 1, 2, 3]),
                             ([], [1])
                         ])

def test_add_front(elements, expected_result):
    ll = LinkedList()
    for i in elements:
        ll.add_back(i)
    ll.add_front(expected_result[0])

    result = []
    iterator = ll.get_head()
    while iterator is not None:
        result.append(iterator.data)
        iterator = iterator.next

    assert result == expected_result

@pytest.mark.parametrize('elements, item_to_remove, expected_result',
                         [
                             ([1, 2, 3], 2, [1, 3]),
                             ([4, 5], 4, [5])
                         ])

def test_remove(elements, item_to_remove, expected_result):
    ll = LinkedList()
    for i in elements:
        ll.add_back(i)

    ll.remove(item_to_remove)

    result = []
    iterator = ll.get_head()
    while iterator is not None:
        result.append(iterator.data)
        iterator = iterator.next

    assert result == expected_result

@pytest.mark.parametrize('elements, item, position, expected_result',
                         [
                             ([1, 3], 2, 1, [1, 2, 3]),
                             ([1, 2, 4], 3, 2, [1, 2, 3, 4])
                         ])

def test_insert_by_position(elements, item, position, expected_result):
    ll = LinkedList()
    for i in elements:
        ll.add_back(i)

    ll.insert_by_position(item, position)

    result = []
    iterator = ll.get_head()
    while iterator is not None:
        result.append(iterator.data)
        iterator = iterator.next

    assert result == expected_result