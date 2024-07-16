def rotate_and_reverse(lst: list[int or float], k: int) -> list:
    is_list_valid(lst)

    length = len(lst)

    for i in range(k):
        last_element = lst[-1]

        for j in range(length - 1, 0, -1):
            lst[j] = lst[j-1]

        lst[0] = last_element

    return lst

def is_list_valid(lst: list[int or float]) -> None:
    for i in lst:
        if not isinstance(i, int or float): raise TypeError()

    if not isinstance(lst, list): raise TypeError()