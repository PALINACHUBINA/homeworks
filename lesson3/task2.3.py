list = []
for num in range(3):
    print('Введите ', num + 1, 'число: ', end = '')
    number = int(input())
    list.append(number)
print('Среднее арифметическое чисел: ', round(sum(list) / len(list), 3))