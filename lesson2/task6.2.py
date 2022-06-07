import math
print('Введите коэффициенты для уравнения: ', end = '')
print('ax^4 + bx^2 + c = 0')
a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))
d = b ** 2 - 4 * a * c

if d < 0:
    print('Уравнение не имеет действительных корней.')
else:
    y_1 = (-b + math.sqrt(d)) / (2 * a)
    y_2 = (-b - math.sqrt(d) / (2 * a))
    if y_1 < 0:
        print('x_1 и x_2 не действительные корни.')
    else:
        x_1 = math.sqrt(y_1)
        x_2 = -x_1
        print('x_1 = ', round(x_1, 3), 'x_2 = ', round(x_2, 3))
    if y_2 < 0:
        print('x_3 и x_4 не действительные корни.')
    else:
         x_3 = math.sqrt(y_2)
         x_4 = -x_3
         print('x_3 = ', round(x_3, 3), 'x_4 = ', round(x_4, 3))






