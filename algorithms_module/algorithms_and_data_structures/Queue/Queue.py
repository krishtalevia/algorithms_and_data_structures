from __future__ import annotations

class Node:
    def __init__(self, data: any, prev=None):
        self.data = data
        self.prev = prev

class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def is_empty(self) -> bool:
        return True if self.__count == 0 else False

    def enqueue(self, data: any) -> None:
        new_node = Node(data)

        if self.is_empty():
            self.__head = new_node
        else:
            self.__tail.prev = new_node

        self.__tail = new_node
        self.__count += 1

    def dequeue(self) -> any:
        if self.is_empty():
            return None

        data = self.__head.data
        self.__head = self.__head.prev

        if self.__head is None:
            self.__tail = None

        self.__count -= 1

        return data

    def peek(self) -> any:
        if self.is_empty():
            return None

        return self.__head.data

    def get_count(self) -> int:
        return self.__count