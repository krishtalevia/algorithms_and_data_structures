def average(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    return round((total / count), 1)