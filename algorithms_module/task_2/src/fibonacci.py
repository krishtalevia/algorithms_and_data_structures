def fibonacci(n: int) -> list:
    is_n_valid(n)

    result = [0, 1]

    if n == 0:
        return [0]
    elif n == 1:
        return result

    for i in range(2, n + 1, 1):
        temp = result[-1] + result[-2]
        result.append(temp)

    return result

def is_n_valid(n: int) -> None:

    if not isinstance(n, int): raise TypeError()

    if n < 0: raise ValueError()

