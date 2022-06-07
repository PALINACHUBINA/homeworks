weight = float(input('Введите массу тела в кг: '))
height = float(input('Введите рост в метрах: '))
age = int(input('Сколько полных лет: '))
BMI = round(weight / height ** 2, 2)
print(BMI)
if age < 45:
    if BMI < 18.5:
        print('Недостаточная масса тела.')
    elif BMI >= 18.5 or BMI <= 24.99:
        print('Норма.')
    elif BMI >= 25 or BMI <= 29.99:
        print('Избыточная масса тела.')
    else:
        print('Ожирение.')

if age >= 45:
    if BMI < 22:
        print('Недостаточная масса тела.')
    elif BMI >= 22 or BMI <= 26.99:
        print('Норма.')
    elif BMI >= 27 or BMI <= 31.99:
        print('Избыточная масса тела.')
    else:
        print('Ожирение.')

