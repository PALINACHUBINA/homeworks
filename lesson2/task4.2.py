import math
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
d = b ** 2 - 4 * a * c
if d > 0:
    x_1 = (-b + math.sqrt(d)) / (2 * a)
    x_2 = (-b - math.sqrt(d)) / (2 * a)
    print('Корни уравнения: ', round(x_1, 3), ',', round(x_2, 3))
elif d == 0:
    x = -b / (2 * a)
    print('Уравнение имеет один корень: ', x)
else:
    print('Уравнение не имеет корней.')