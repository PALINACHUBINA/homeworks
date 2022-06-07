import math
print('Введите коэффициенты для уравнения: ')
a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))
d = b ** 2 - 4 * a * c

if d > 0:
    x_1 = (-b + math.sqrt(d) / (2 * a))
    x_2 = (-b - math.sqrt(d) / (2 * a))
    print('Уравнение имеет два корня: ', round(x_1, 3), ',', round(x_2, 3))
elif d == 0:
    x_1 = -b / (2 * a)
    print('Уравнение имеет один корень: ', round(x_1, 2))
else:
    print('Уравнение не имеет корней.')
