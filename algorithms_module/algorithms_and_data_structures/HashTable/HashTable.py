from __future__ import annotations

class HashTable:
    def __init__(self, size=10) -> None:
        self.__count = 0
        self.__size = size
        self.__table = [None] * self.__size

    def __hash(self, key: any) -> int:
        first_hash = hash(key)
        return first_hash % self.__size

    def add(self, key: any, value: any) -> None:
        hash = self.__hash(key)
        print(f'HASHMAP:ADD:HASH:{hash}')

        if not (self.__table[hash] is None):
            print(f'HASHMAP:ADD:COLLISION:{hash}')
            return

        self.__table[hash] = value

    def get(self, key: any) -> any:
        hash = self.__hash(key)
        if self.__table[hash] is None:
            raise Exception('Ключ не найден!')

        return self.__table[hash]

    def delete(self, key: any) -> None:
        hash = self.__hash(key)
        if self.__table[hash] is None:
            raise Exception('Ключ не найден!')

        del self.__table[hash]

    def __str__(self) -> str:
        return str(self.__table)