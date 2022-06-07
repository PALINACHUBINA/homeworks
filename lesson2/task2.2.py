while True:
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
    summa = number_1 + number_2
    if 100 >= summa >= 10:
        print('Выполнено успешно. Сумма чисел: ', summa)
    else:
        print('Сумма чисел не вошла в диапазон.')
    print()