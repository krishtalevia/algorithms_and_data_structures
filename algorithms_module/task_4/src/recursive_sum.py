def recursive_sum(lst: list[int]) -> int:
    assert isinstance(lst, list), TypeError()

    for i in lst:
        assert isinstance(i, int), TypeError()

    if len(lst) == 0:
        return 0

    return lst[0] + recursive_sum(lst[1:])