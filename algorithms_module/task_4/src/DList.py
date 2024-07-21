def malloc(memory: int, size=1) -> list:
    assert size > 0, ValueError()

    return [None] * size

class DList:

    def __init__(self, n: int or list[any]):
        if isinstance(n, int):
            self.__size = n + (n // 2)
            self.__count = 0

        elif isinstance(n, list):
            self.__size = len(n) + (len(n) // 2)
            self.__count = len(n)
            self.__array_memory = n + [None] * (self.__size - len(n))
            return
        else:
            raise TypeError()

        self.__array_memory = None
        if self.__size != 0:
            self.__array_memory = malloc(4, self.__size)

    def add(self, item: any) -> None:
        if self.__count >= self.__size:
            self.__realloc()

        self.__array_memory[self.__count] = item
        self.__count += 1

    def add_front(self, item: any):
        pass

    def remove(self, index: int) -> bool:
        pass

    def remove_of_index(selfi, index: int):
        pass

    def find(self, item: any):
        pass

    def insert_to_index(self, item: any, index: int) -> bool:
        assert index >= 0, ValueError()

        if self.__count == 0:
            self.add(item)
            return True

        if index >= self.__count:
            self.add(item)
            return True

        if self.__count == self.__size:
            self.__realloc()

        for i in range(self.__count, index, -1):
            self.__array_memory[i] = self.__array_memory[i - 1]

        self.__array_memory[index] = item

    def is_empty(self):
        pass

    def __realloc(self):
        self.__size = self.__size + (self.__size // 2)
        new_memory = malloc(4, self.__size)

        for i in range(0, self.__count, 1):
            new_memory[i] = self.__array_memory[i]

        self.__array_memory = new_memory

    def __get_size(self):
        return self.__size

    def __get_count(self):
        return self.__count