def most_frequency_occuring_element(list: list) -> int:
    if not is_list_valid(list):
        raise Exception('Ошибка!')

    buff = 0
    frequency = 0
    answer = list[0]

    for i in range(0, len(list), 1):
        for j in range(0, len(list), 1):
            if list[i] == list[j]:
                buff += 1

        if buff > frequency:
            frequency = buff
            answer = list[i]

        if frequency == buff:
            if answer > list[i]:
                answer = list[i]

        buff = 0

    return answer

def is_list_valid(list: list) -> bool:
    for i in range(0, len(list), 1):
        if not isinstance(list[i], int):
            return False

        elif list[i] < 1 or list[i] > (2 * 10 ** 4):
            return False

    return True