def large_integer(digits: list) -> list:
    is_list_valid(digits)

    if len(digits) == 0:
        return []

    if digits[-1] != 9:
        digits[-1] += 1

        return digits

    for i in range(len(digits)-1, 0, -1):
        digits[i] += 1

        if digits[i] == 10:
            digits[i] = 0
            digits[i-1] += 1

    if digits[0] == 10:
        digits[0] = 1
        digits.append(0)

    return digits

def is_list_valid(digits: list) -> None:
    if not isinstance(digits, list): raise TypeError()

    if len(digits) < 1 or len(digits) > 100: raise ValueError()

    for i in digits:
        if not isinstance(i, int): raise TypeError()

        if i < 0 or i > 9: raise ValueError()

    for i in range(0, len(digits)-1, 1):
        if digits[i] < digits[i+1]: raise ValueError()