name = input('Введите имя: ')
age = int(input('Введите возраст: '))
city = input('Введите город: ')

#print('Меня зовут %s. Мне %s лет. Я живу в городе %s.'%(name, age, city))

#print('Меня зовут {}. Мне {} лет. Я живу в городе {}.'.format(name, age, city))

print(f'Меня зовут {name}. Мне {age} лет. Я живу в городе {city}.')