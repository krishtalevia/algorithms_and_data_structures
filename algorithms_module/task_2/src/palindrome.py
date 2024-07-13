def palindrome(x: int) -> bool:
    is_x_valid(x)

    temp_x = x
    reversed_x = 0
    while temp_x > 0:
        digit = temp_x % 10
        reversed_x = reversed_x * 10 + digit
        temp_x //= 10

    if reversed_x == x:
        return True

    return False

def is_x_valid(x: int) -> None:
    if not isinstance(x, int): raise TypeError()