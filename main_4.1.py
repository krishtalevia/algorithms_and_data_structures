import math

print('Введите коэффициенты a, b и c для уравнения ax^2 + bx + c = 0')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    root_1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root_2 = (-b - math.sqrt(discriminant)) / (2 * a)

    print('Корни уравнения: ', root_1, 'и', root_2)

elif discriminant == 0:
    root = -b / 2 * a

    print('Единственный корень уравнения: ', root)

else:
    print('У уравнения нет действительных корней')
