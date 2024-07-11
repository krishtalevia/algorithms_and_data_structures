def count_ones(n: int) -> int:
    is_n_valid(n)

    result = ''

    while n > 0:
        if n % 2 == 0:
            result += '0'
        else:
            result += '1'

        n = n // 2

    result = result[::-1]
    return int(result)

def is_n_valid(n: int) -> None:
    if not isinstance(n, int): raise TypeError()

    if n <= 0: raise ValueError()