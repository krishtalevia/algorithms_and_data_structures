def sum_of_digits(n: int) -> int:
    assert isinstance(n, int), TypeError

    s = str(n)

    if len(s) <= 1:
        return n

    return int(s[0]) + sum_of_digits(int(s[1::]))