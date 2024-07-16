def max_in_range(lst: list[int or float], start: int, end: int) -> list:
    is_request_valid(lst, start, end)

    max_value = lst[start]
    absolute_index = start
    relative_index = 0

    for i in range(start, end + 1, 1):
        if lst[i] > max_value:
            max_value = lst[i]
            absolute_index = i
            relative_index = i - start

    return [max_value, absolute_index, relative_index]

def is_request_valid(lst: list[int or float], start, end) -> None:
    if not isinstance(lst, list): raise TypeError()

    for i in lst:
        if not isinstance(i, int or float): raise TypeError()

    if start < 0 or start > len(lst): raise ValueError()
    if end < 0 or end > len(lst): raise ValueError()
    if start > end: raise ValueError()