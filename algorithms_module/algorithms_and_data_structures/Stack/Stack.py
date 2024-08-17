from __future__ import annotations

from typing import List, Any


class Node:
    def __init__(self, data: any):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.__top = None
        self.__size = 0

    def is_empty(self) -> bool:
        if self.__size == 0:
            return True

        return False

    def push(self, data: any) -> None:
        new_node = Node(data)
        new_node.next = self.__top
        self.__top = new_node
        self.__size += 1

    def pop(self) -> any:
        if self.__size == 0:
            return None
        else:
            removed_node = self.__top.data
            self.__top = self.__top.next
            self.__size -= 1
            return removed_node

    def peek(self) -> any:
        if self.__size == 0:
            return None
        else:
            return self.__top.data

    def __str__(self) -> list[any]:
        nodes = []

        iterator = self.__top
        while iterator.next is not None:
            nodes.append(iterator)
            iterator = iterator.next

        return nodes