string = '@//^(&&#@!/*)+-/'
print(string)
first = string.find('(')
second = string.find(')')

print(string[first + 1:second])
