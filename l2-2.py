userStr = input('Введите элементы списка через пробел:')

my_list = userStr.split()
print(my_list)
j = 0
for i in range(int(len(my_list) // 2)):
    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    j += 2

print(my_list)
