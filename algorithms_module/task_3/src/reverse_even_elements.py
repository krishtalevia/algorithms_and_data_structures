def reverse_even_elements(array: list[int or float]) -> list:
    is_array_valid(array)

    even_elements = []
    for i in array:
        if i % 2 == 0:
            even_elements.append(i)

    for i in range(0, len(even_elements), 1):
        for j in range(0, len(even_elements)-i-1, 1):
            if even_elements[j] < even_elements[j+1]:
                even_elements[j], even_elements[j+1] = even_elements[j+1], even_elements[j]

    remaining_elements = 0
    while remaining_elements != len(even_elements):
        for i in range(0, len(array), 1):
            if array[i] % 2 == 0:
                array[i] = even_elements[remaining_elements]

                remaining_elements += 1

    return array

def is_array_valid(array: list[int or float]) -> None:
    for i in array:
        if not isinstance(i, int or float): raise TypeError()