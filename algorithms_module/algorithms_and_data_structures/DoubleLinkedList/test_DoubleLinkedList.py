import pytest
from algorithms_module.algorithms_and_data_structures.DoubleLinkedList.DoubleLinkedList import DoubleLinkedList

@pytest.mark.parametrize('elements, expected_result',
                         [
                             ([1, 2, 3], False),
                             ([], True)
                         ])

def test_is_empty(elements, expected_result):
    dll = DoubleLinkedList()
    for i in elements:
        dll.add_back(i)
    assert dll.is_empty() == expected_result

@pytest.mark.parametrize('elements, expected_result',
                         [
                             ([1, 2, 3], [1, 2, 3, 4]),
                             ([], [1])
                         ])

def test_add_back(elements, expected_result):
    dll = DoubleLinkedList()
    for i in elements:
        dll.add_back(i)
    dll.add_back(expected_result[-1])

    result = []
    iterator = dll.get_head()
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
    dll = DoubleLinkedList()
    for i in elements:
        dll.add_back(i)
    dll.add_front(expected_result[0])

    result = []
    iterator = dll.get_head()
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
    dll = DoubleLinkedList()
    for i in elements:
        dll.add_back(i)

    dll.remove(item_to_remove)

    result = []
    iterator = dll.get_head()
    while iterator is not None:
        result.append(iterator.data)
        iterator = iterator.next

    assert result == expected_result

@pytest.mark.parametrize('elements, item_to_find, expected_result',
                         [
                             ([1, 3], 2, False),
                             ([1, 2, 4], 2, True)
                         ])

def test_find(elements, item_to_find, expected_result):
    dll = DoubleLinkedList()
    for i in elements:
        dll.add_back(i)

    node = dll.find(item_to_find)

    assert node == expected_result