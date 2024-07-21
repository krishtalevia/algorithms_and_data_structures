def recursive_max(lst: list[int]) -> int:
    assert isinstance(lst, list), TypeError()

    for i in lst:
        assert isinstance(i, int), TypeError()

    if len(lst) == 0:
        return 0

    return lst[0] if lst[0] > recursive_max(lst[1:]) else recursive_max(lst[1:])