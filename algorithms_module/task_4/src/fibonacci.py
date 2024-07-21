def fibonacci(n: int) -> list[int]:
    assert isinstance(n, int), TypeError()

    assert n >= 0, ValueError()

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)