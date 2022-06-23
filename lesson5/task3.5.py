list = [-12, 77, 95, 11, 33, -22, -4, 17, 14, 12]
max_num = max(list)
print('Максимальный элемент в списке: ', max_num)
index = list.index(max_num)
list.pop(index)
list.insert(0, max_num)

print('Новый список: ', list)


