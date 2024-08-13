from __future__ import annotations

class Node:
    def __init__(self, data: any) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.__head = None
        self.__count = 0

    def is_empty(self) -> bool:
        if self.__count == 0:
            return False

        return True

    def add_back(self, item: any) -> None:
        new_node = Node(data=item)
        if self.__count == 0:
            self.__head = new_node
            self.__count += 1
        else:
            iterator = self.__head
            while not (iterator is None):
                iterator = iterator.next
            iterator.next = new_node

    def add_front(self, item: any) -> None:
        new_node = Node(item)
        new_node.next = self.__head
        self.__head = new_node

    def remove(self, item: any) -> bool:
        if self.__count == 0:
            return False

        iterator = self.__head
        iterator_prev = None

        while iterator.data != item and not (iterator.next is None):
            iterator_prev = iterator
            iterator = iterator.next

            if iterator.data == item:
                iterator_prev.next = iterator.next
                self.__count -= 1
                return True

            return False

    def insert_by_position(self, item: any, position: int) -> bool:
        if position > self.__count or position < 0:
            return False

        new_node = Node(data=item)

        if position == 0:
            new_node.next = self.__head
            self.__head = new_node
            return True

        iterator = self.__head
        count = 0

        while iterator.data is not None and count < self.__count -1:
            iterator = iterator.next
            count += 1

        new_node.next = iterator.next
        iterator.next = new_node

    def count(self, item: any) -> int:
        if self.__head is None:
            return 0

        iterator = self.__head
        count = 0
        while iterator.data is not None:
            count += 1
            iterator = iterator.next
        return count
        
    def is_empty(self) -> bool:
        return True if self.__count == 0 else False

    def clear(self):
        self.__head = None
        self.__count = 0