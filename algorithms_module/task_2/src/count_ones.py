def count_ones(n: int) -> int:
    is_n_valid(n)

    count = 0

    while n > 0:
        if n % 2 != 0:
            count += 1

        n = n // 2

    return count

def is_n_valid(n: int) -> None:
    if not isinstance(n, int): raise TypeError()

    if n <= 0: raise ValueError()
    
