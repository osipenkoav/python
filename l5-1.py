userStr = None
f = open('test_1.txt', 'w')
while userStr != '':
    userStr = input('Введите строку (пустая строка - для выхода): ')
    f.write(userStr + '\n')
f.close()
