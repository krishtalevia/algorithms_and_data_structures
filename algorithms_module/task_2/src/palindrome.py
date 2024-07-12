def palindrome(x: int) -> bool:
    is_x_valid(x)

    reversed_x = 0
    while x > 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x //= 10

    if reversed_x == x:
        return True

    return False

def is_x_valid(x: int) -> None:
    if not isinstance(x, int): raise TypeError()

print(palindrome(12321))