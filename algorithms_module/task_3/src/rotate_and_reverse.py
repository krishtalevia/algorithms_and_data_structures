def rotate_and_reverse(array: list[int or float], k: int) -> list:
    is_list_valid(array)

    length = len(array)

    for i in range(k):
        last_element = array[-1]

        for j in range(length - 1, 0, -1):
            array[j] = array[j-1]

        array[0] = last_element

    return array

def is_list_valid(array: list[int or float]) -> None:
    for i in array:
        if not isinstance(i, int or float): raise TypeError()