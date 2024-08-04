from __future__ import annotations

class PrintDocument:

    def __init__(self, title: str, number_of_pages: int):
        self.__title = title
        self.__number_of_pages = number_of_pages

class Node:

    def __init__(self, data: PrintDocument, prev=None):
        self.data = data
        self.prev = prev

class PrintQueue:

    def __init__(self):
        self.__head = None
        self.__tail = None

        self.__count = 0

    def enqueue(self, document: PrintDocument) -> None:
        node = Node(data=document, prev=None)

        if self.is_empty():
            self.__head = node
        else:
            self.__tail.prev = node

        self.__tail = node

        self.__count += 1

    def dequeue(self) -> any:
        if self.is_empty():
            return None

        data = self.__head.data
        self.__head = self.__head.prev

        if self.__count == 1:
            self.__tail = None

        self.__count -= 1

        return data

    def peek(self) -> any:
        if self.is_empty():
            return None

        return self.__head.data

    def is_empty(self) -> bool:
        return True if self.__count == 0 else False

    def count(self) -> int:
        return self.__count
