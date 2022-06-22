string = input('Введите строку или слово: ')

if string == "".join(reversed(string)):
    print('Палиндром.')
else:
    print('Не палиндром.')


