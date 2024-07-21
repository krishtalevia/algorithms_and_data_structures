def selection_sort_with_counts(array: list[any], key=lambda x: x, order_by=lambda x, y: x >y) -> list[any]:
    assert isinstance(array, list), TypeError()

    length = len(array)
    comparisons = 0
    swaps = 0

    if length == 0:
        return []

    if length == 1:
        return array

    for i in range(0, length -1, 1):
        imin = i

        for j in range(i+1, length, 1):
            if order_by(key(array[imin]), key(array[j])):
                imin = j
                comparisons += 1

        array[i], array[imin] = array[imin], array[i]
        swaps += 1

    return array, comparisons, swaps