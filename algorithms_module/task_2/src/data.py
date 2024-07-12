with open('data.txt', 'r') as file:
    base_data = file.read()

data = []
base_data = base_data.split('\n')
for i in base_data:
    temp = i.split(',')
    data.append(temp)

days = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
count = 0

for i in data:
    i.append(days[count])
    count += 1

    if count == 6:
        count = 0

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

print(months_traffic)