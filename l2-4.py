userString = input('Введите слова через пробел: ')

list1 = userString.split()

for i, s in enumerate(list1):
    print(i, s[:10])
