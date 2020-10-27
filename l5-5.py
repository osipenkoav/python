userInp = input('Введите числа разделенные пробелом: ')
f = open('test5.txt', 'w')
f.write(userInp)
f.close()

f1 = open('test5.txt', 'r')
str1 = f1.read()
f1.close()

summa = 0
for i in str1.split():
    summa = summa + int(i)
print(f'сумма числе в файле: {summa}')
