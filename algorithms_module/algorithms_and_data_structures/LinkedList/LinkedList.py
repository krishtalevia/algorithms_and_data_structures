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
            return True

        return False

    def add_back(self, item: any) -> None:
        new_node = Node(data=item)
        if self.__count == 0:
            self.__head = new_node
        else:
            iterator = self.__head
            while not (iterator.next is None):
                iterator = iterator.next
            iterator.next = new_node
        self.__count += 1

    def add_front(self, item: any) -> None:
        new_node = Node(item)
        new_node.next = self.__head
        self.__head = new_node
        self.__count += 1

    def remove(self, item: any) -> bool:
        if self.__count == 0:
            return False

        if self.__head.data == item:
            self.__head = self.__head.next
            self.__count -= 1
            return True

        iterator = self.__head
        while iterator.next is not None:
            if iterator.next.data == item:
                iterator.next = iterator.next.next
                self.__count -= 1
                return True
            iterator = iterator.next

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
        for i in range(position -1):
            iterator = iterator.next
        new_node.next = iterator.next
        iterator.next = new_node

    def count(self) -> int:
        if self.__head is None:
            return 0

        iterator = self.__head
        count = 0
        while iterator.data is not None:
            count += 1
            iterator = iterator.next
        return count

    def clear(self):
        self.__head = None
        self.__count = 0

    def get_head(self):
        return self.__head

    def __str__(self):
        elements = []
        iterator = self.__head
        while iterator is not None:
            elements.append(str(iterator.data))
            iterator = iterator.next
        return ' -> '.join(elements)