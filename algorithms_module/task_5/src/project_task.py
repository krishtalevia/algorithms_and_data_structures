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

class TaskStack:

    def __init__(self):
        self.__array = []

    def push(self, task: ProjectTask):
        self.__array.append(task)

    def pop(self):
        if len(self.__array) == 0:
            return None

        return self.__array.pop(-1)

    def peek(self):
        if len(self.__array) == 0:
            return None

        return self.__array[-1]

    def is_empty(self):
        return True if len(self.__array) == 0 else False

    def __get_count(self):
        return len(self.__array)
