a = float(input('Введите первую сторону треугольника: '))
b = float(input('Введите первую сторону треугольника: '))
c = float(input('Введите первую сторону треугольника: '))
if (a + b > c) and (a + c > b) and (b + c > a):
    print('Треугольник существует.')
else:
    print('Треугольник не существует.')
if a != b and a != c and b != c:
    print('Треугольник разносторонний.')
elif (a ==b or a == c) and (b == a or b == c) and (c == a or c == b):
    print('Треугольник равнобедренный.')
elif a == b and a == c:
    print('Треугольник равносторонний.')