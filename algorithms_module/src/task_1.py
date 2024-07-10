# Задание №1
def even_sum(list: list) -> int:
    if not is_list_valid(list):
        raise Exception('Ошибка!')

    even_sum = 0

    for i in range(0, len(list), 1):
        if list[i] % 2 == 0:
            even_sum += list[i]

    if even_sum <= 0:
        return 1

    return even_sum

def is_list_valid(list: list) -> bool:
    if len(list) > 10**5:
        return False

    for i in range(0, len(list), 1):
        if not isinstance(list[i], int):
            return False

        elif list[i] < (-2*10**4) or list[i] > (2*10**4):
            return False

    return True

print(even_sum(['']))