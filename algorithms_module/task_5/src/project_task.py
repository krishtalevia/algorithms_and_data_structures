from __future__ import annotations

class DateTime:

    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

class ProjectTask:

    def __init__(self, description: str, due_date: DateTime):
        self.__description = description
        self.__due_date = due_date

class Node:

    def __init__(self, task: ProjectTask):
        self.task = task
        self.next = None

class TaskStack:

    def __init__(self):
        self.__top = None
        self.__size = 0

    def push(self, task: ProjectTask):
        node = Node(task)
        node.next = self.__top
        self.__top = node
        self.__size += 1

    def pop(self):
        if self.__size == 0:
            return None

        removed_task = self.__top.task
        self.__top = self.__top.next
        self.__size -= 1
        return removed_task

    def peek(self):
        if self.__size == 0:
            return None

        return self.__top.task

    def is_empty(self):
        return True if self.__size == 0 else False

    def count(self):
        return self.__size