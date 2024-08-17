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
        hash_index = self.__hash(key)
        print(f'HASHMAP:ADD:HASH:{hash_index}')

        if self.__table[hash_index] is not None:
            print(f'HASHMAP:ADD:COLLISION:{hash_index}')
            return

        self.__table[hash_index] = value
        self.__count += 1

    def get(self, key: any) -> any:
        hash_index = self.__hash(key)
        if self.__table[hash_index] is None:
            raise KeyError('Ключ не найден!')

        return self.__table[hash_index]

    def delete(self, key: any) -> None:
        hash_index = self.__hash(key)
        if self.__table[hash_index] is None:
            raise KeyError('Ключ не найден!')

        del self.__table[hash_index]
        self.__count -= 1

    def __str__(self) -> str:
        return str(self.__table)