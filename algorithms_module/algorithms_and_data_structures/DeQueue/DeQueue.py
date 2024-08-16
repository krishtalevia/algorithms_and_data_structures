from __future__ import annotations

class Node:
    def __init__(self, data: any):
        self.data = data
        self.prev = None
        self.next = None

class Dequeue:
    def __init__(self) -> None:
        self.__head = None
        self.__tail = None

    def is_empty(self) -> bool:
        if self.__head is None:
            return False

        return True

    def add_front(self, data: any) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node

    def add_rear(self, data: any) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.prev = self.__tail
            self.__tail.next = new_node
            self.__tail = new_node

    def remove_front(self) -> any:
        if self.is_empty():
            return None

        data = self.__head.data
        self.__head = self.__head.next

        if self.__head is None:
            self.__tail = None
        else:
            self.__head.prev = None

        return data

    def remove_rear(self) -> any:
        if self.is_empty():
            return None

        data = self.__tail.data
        self.__tail = self.__tail.prev

        if self.__tail is None:
            self.__head = None
        else:
            self.__tail.next = None

        return data

    def peek_front(self) -> any:
        if self.is_empty():
            return None
        return self.__head.data

    def peek_rear(self) -> any:
        if self.is_empty():
            return None
        return self.__tail.data

    def __str__(self) -> list[str]:
        nodes = []
        iterator = self.__head
        while iterator is not None:
            nodes.append(str(iterator.data))
            iterator = iterator.next

        return nodes
