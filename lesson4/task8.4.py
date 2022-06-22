password = input('Введите пароль: ')

special_symbols = ['@', '#', '%', '&']
up_letters = 0
low_letters = 0
number = 0
symbol_count = 0

for symbol in password:
    if symbol.isupper():
        up_letters += 1
    elif symbol.islower():
        low_letters += 1
    elif symbol.isdigit():
        number += 1
    elif symbol in special_symbols:
        symbol_count += 1

if (len(password) >= 5) and (up_letters >= 1) and (low_letters >= 1) and (number > 1) and (symbol_count >= 1):
    print('Пароль сложный.')
else:
    print('Пароль простой.')

