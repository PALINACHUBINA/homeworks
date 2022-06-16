list = []
for i in range(3):
    print('Введите ', i + 1, 'число: ', end = '')
    number = int(input())
    list.append(number)

negative = 0
positive = 0
for i_num in range(3):
    if list[i_num] > 0:
        positive += 1
    else:
        negative += 1
print(f'Положительных: %s, отрицательных: %s' %(positive, negative))


