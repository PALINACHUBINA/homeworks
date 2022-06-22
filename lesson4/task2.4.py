string = 'Мама любит молоко.'
print(string.upper())
string_2 = input('Введите строку: ')
result = string.find(string_2)
if result == -1:
    print('Строки нет.')
else:
    print('Строка есть.')