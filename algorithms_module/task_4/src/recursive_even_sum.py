def recursive_even_sum(lst: list[int]) -> int:
    assert isinstance(lst, list), TypeError()

    for i in lst:
        assert isinstance(i, int), TypeError()

    if len(lst) == 0:
        return 0

    if lst[0] % 2 == 0:
        return lst[0] + recursive_even_sum(lst[1:])
    else:
        return recursive_even_sum(lst[1:])