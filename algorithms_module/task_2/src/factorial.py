def factorial(n: int) -> int:
    is_n_valid(n)

    result = 1

    for i in range(1, n+1, 1):
        result *= i

    return result

def is_n_valid(n: int) -> None:
    if not isinstance(n, int): raise TypeError()

    if n <= 0 or n >= 20: raise ValueError()