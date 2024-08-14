from __future__ import annotations

class Node:
    def __init__(self, data: any):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.__top = None
        self.__size = 0

    def push(self, data: any) -> None:
        pass

    def pop(self) -> any:
        pass

    def peek(self) -> any:
        pass

    def __str__(self) -> str:
        pass