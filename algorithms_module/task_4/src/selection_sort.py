def selection_sort(array: list[any], key=lambda x: x, order_by=lambda x, y: x >y) -> list[any]:
    assert isinstance(array, list), TypeError()

    length = len(array)

    if length == 0:
        return []

    if length == 1:
        return array

    for i in range(0, length -1, 1):
        imin = i

        for j in range(i+1, length, 1):
            if order_by(key(array[imin]), key(array[j])):
                imin = j

        array[i], array[imin] = array[imin], array[i]

    return array