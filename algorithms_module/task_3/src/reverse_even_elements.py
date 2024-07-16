def reverse_even_elements(lst: list[int or float]) -> list:
    is_array_valid(lst)

    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst[0]]

    even_elements = []
    for i in lst:
        if i % 2 == 0:
            even_elements.append(i)

    for i in range(0, len(even_elements), 1):
        for j in range(0, len(even_elements)-i-1, 1):
            if even_elements[j] < even_elements[j+1]:
                even_elements[j], even_elements[j+1] = even_elements[j+1], even_elements[j]

    remaining_elements = 0
    while remaining_elements != len(even_elements):
        for i in range(0, len(lst), 1):
            if lst[i] % 2 == 0:
                lst[i] = even_elements[remaining_elements]

                remaining_elements += 1

    return lst

def is_array_valid(lst: list[int or float]) -> None:
    for i in lst:
        if not isinstance(i, int or float): raise TypeError()

    if not isinstance(lst, list): raise TypeError()