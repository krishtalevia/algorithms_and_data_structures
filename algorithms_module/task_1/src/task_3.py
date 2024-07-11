def target_sum(list: list, target: int) -> list:
    if not is_list_valid(list):
        raise Exception('Ошибка!')

    for i in range(0, len(list), 1):
        for j in range(i + 1, len(list), 1):
            if (list[i] + list[j]) == target:
                return [i,j]

    raise Exception('Ошибка!')

def is_list_valid(list: list) -> bool:
    for i in range(0, len(list), 1):
        if not isinstance(list[i], int):
            return False

        elif list[i] <= -109 or list[i] >= 109:
            return False

        elif list[i] < 2 or list[i] > 104:
            return False

    return True
