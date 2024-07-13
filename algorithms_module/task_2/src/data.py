def read_data(file_name: str) -> list:
    with open('data.txt', 'r') as file:
        base_data = file.read()

    data = []
    base_data = base_data.split('\n')
    for i in base_data:
        temp = i.split(',')
        data.append(temp)

    return data

def expend_data_with_days(data: list) -> list:
    days = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
    count = 0

    for i in data:
        i.append(days[count])
        count += 1

        if count == 6:
            count = 0

    return data

def max_month(data: list) -> str:

    months_traffic = {'01': ['Январь', 0], '02': ['Февраль', 0], '03': ['Март', 0],
              '04': ['Апрель', 0], '05': ['Май', 0], '06': ['Июнь', 0],
              '07': ['Июль', 0], '08': ['Август', 0], '09': ['Сентябрь', 0],
              '10': ['Октябрь', 0], '11': ['Ноябрь', 0], '12': ['Декабрь', 0]}

    sum = 0
    current_month = data[0][0][5:7]

    for i in data:
       month = i[0][5:7]

       if month != current_month:
           months_traffic[current_month][1] += sum
           sum = 0
           current_month = month

       sum += int(i[1])

    months_traffic[current_month][1] += sum

    max_month = 'Январь'
    max_traffic = 0
    for i in months_traffic:
        traffic = months_traffic[i][1]
        if traffic > max_traffic:
            max_traffic = traffic
            max_month = months_traffic[i][0]

    return max_month

def max_day(data: list) -> str:
    days_traffic = {'Понедельник': 0, 'Вторник': 0, 'Среда': 0,
                    'Четверг': 0, 'Пятница': 0, 'Суббота': 0,
                    'Воскресенье': 0}

    sum = 0
    current_day = data[0][2]

    for i in data:
       day = i[2]

       if day != current_day:
           days_traffic[current_day] += sum
           sum = 0
           current_day = day

       sum += int(i[1])

    days_traffic[current_day] += sum

    max_day = 'Воскресенье'
    max_traffic = 0
    for i in days_traffic:
        traffic = days_traffic[i]
        if traffic > max_traffic:
            max_traffic = traffic
            max_day = i

    return max_day

def main():
    data = read_data('data.txt')
    data = expend_data_with_days(data)
    print(max_day(data))
    print(max_month(data))

main()