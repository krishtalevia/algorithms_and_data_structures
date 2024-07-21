def bubble_sort(array: list[any], key=lambda x: x, order_by=lambda x, y: x > y) -> list[any]:
    assert isinstance(array, list), TypeError()

    length = len(array)

    if length == 0:
        return []

    if length == 1:
        return array

    for i in range(0, length, 1):
        for j in range(0, length-i-1, 1):
            if order_by(key(array[j]), key(array[j+1])):
                array[j], array[j+1] = array[j+1], array[j]

    return array