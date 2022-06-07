list = []
a = int(input('Введите первое число: '))
list.append(a)
b = int(input('Введите второе число: '))
list.append(b)
c = int(input('Введите третье число: '))
list.append(c)
print(list)
max_num = max(list)
min_num = min(list)
print('Максимально число: ', max_num, ', минимально число: ', min_num)
for num in list:
    if num != max_num and num != min_num:
        average_num = num
half_sum = (average_num + min_num) / 2
prod_num = average_num * min_num
if min_num > 1 or min_num % 10 == 0:
    print('Число больше 1 и чётное.')
else:
    print('Число меньше 1 и не чётное.')
if max_num > half_sum or max_num < prod_num:
    print('Число больше полусуммы и меньше произведения чисел.')
else:
    print('Число меньше полусуммы и больше произведения.')
if average_num % 3 == 0 or average_num % 10 == 0:
    print('Число чётное и делиться на 3.')
else:
    print('Число не чётное и не делиться на 3.')