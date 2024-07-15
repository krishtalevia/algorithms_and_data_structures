def max_in_range(list: list[int or float], start: int, end: int) -> list:
    is_list_valid(list)

    end += -len(list)
    max = list[start]
    absolute_index = 0
    relative_index = 0
    for i in range(start, len(list) + end, 1):
        if list[i] > max:
            max = list[i]
            absolute_index = i
            relative_index = i - start

    return [max, absolute_index, relative_index]

def is_list_valid(list: list[int or float]) -> None:
    for i in list:
        if not isinstance(i, int or float): raise TypeError()