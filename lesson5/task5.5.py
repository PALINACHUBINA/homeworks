list = [-2, 17, 3, -9, 14, -77, 65, 8, 12, 44]
index = list.index(min(list))
del list[:index]
print('Новый список: ', list)


