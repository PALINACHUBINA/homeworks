first_list = [1, -11, 2, -7, 14, 55, 4, 11, -22, 12]
index = first_list.index(max(first_list))
new_list = first_list[index:]
del first_list[5:]
second_list = []

for index in new_list:
    if index >= 0:
        second_list.append(index)
    else:
        first_list.append(index)
second_list.extend(first_list)
print('Новый список: ', second_list)






