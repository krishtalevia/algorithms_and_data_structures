import math

# 1

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

# 2 (Площадь треугольника)

print ('Введите длины сторон треугольника a, b и c')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if (c <= a + b) or (b <= a + c) or (a <= b + c):
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('Площадь треугольника: ', area)
    