def max_in_range(list: list[int or float], start: int, end: int) -> list:
    is_request_valid(list, start, end)

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

def is_request_valid(list: list[int or float], start, end) -> None:
    for i in list:
        if not isinstance(i, int or float): raise TypeError()

    if start < 0 or start > len(list): raise ValueError()
    if end < 0 or end > len(list): raise ValueError()
    if start > end: raise ValueError()