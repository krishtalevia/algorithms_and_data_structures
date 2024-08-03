from __future__ import annotations

class PersonCard:

    def __init___(self, name: str, age: int, occupation: str):
        self.__name = name
        self.__age = age
        self.__occupation = occupation

class Node:

    def __init__(self, person_card=None, next: Node=None):
        self.person_card = person_card
        self.next = next

class LinkedList:

    def __init__(self):
        self.__head = None
        self.__count = 0

    def add_back(self, item: PersonCard) -> None:
        node = Node(person_card=item, next=None)

        self.__count += 1

        if self.__count == 0:
            self.__head = node
            return

        iterator = self.__head
        while not (iterator.next is None):
            iterator = iterator.next
        iterator.next = node

    def add_front(self, item: PersonCard) -> None:
        node = Node(person_card=item, next=self.__head)
        self.__head == node
        self.__count += 1

    def remove(self, item) -> bool:
        if self.__count == 0: return False

        iterator = self.__head
        iterator_prev = None

        while iterator.person_card != item and not (iterator.next is None):
            iterator_prev = iterator
            iterator = iterator.next

        if iterator.person_card == item:
            iterator_prev.next = iterator.next
            self.__count -= 1
            return True

        return False

    def insert_by_position(self, item: PersonCard, position: int) -> bool:
        if position < 0 or position > self.__count:
            return False

        if position == 0:
            self.add_front(item)
            return True

        node = Node(person_card=item)
        iterator = self.__head

        for i in range(0, position - 1, 1):
            iterator = iterator.next

        node.next = iterator.next
        iterator.next = node
        self.__count += 1
        return True

    def count(self, item: PersonCard) -> int:
        count = 0

        iterator = self.__head

        while iterator is not None:
            if iterator.person_card == item:
                count += 1
            iterator = iterator.next

        return count

    def is_empty(self) -> bool:
        return True if self.__count == 0 else False

    def clear(self) -> None:
        self.__head = None
        self.__count = 0