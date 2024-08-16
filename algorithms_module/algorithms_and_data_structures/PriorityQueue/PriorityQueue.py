from __future__ import annotations

class Node:
    def __init__(self, data: any, priority: int) -> None:
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self) -> None:
        self.__head = None

    def is_empty(self) -> bool:
        if self.__head is None:
            return False
        return True

    def enqueue(self, data: any, priority: int) -> None:
        new_node = Node(data, priority)

        if self.is_empty() or self.__head.priority > priority:
            new_node.next = self.__head
            self.__head = new_node
        else:
            iterator = self.__head
            while iterator.next is not None and iterator.next.priority <= priority:
                iterator = iterator.next
            new_node.next = iterator.next
            iterator.next = new_node

    def dequeue(self) -> any:
        if self.is_empty():
            return None
        data = self.__head.data
        self.__head = self.__head.next
        return data

    def peek(self) -> any:
        if self.is_empty():
            return None
        return self.__head.data