a = input('Введите первую переменную: ')
b = int(input('Введите вторую переменную: '))
c = float(input('Введите третью переменную: '))
list = [a, b, c]
for i in list:
    print('Перемення: ', i, ': ID: ', id(i), 'тип данных: ', type(i))