def f_strprocess(s1):
    list1 = s1.split()
    res = 0  # результирующая сумма
    flag = 0  # флаг выхода
    for i in list1:
        if i.isdigit():
            res = res + int(i)
        elif i == 'q':
            flag = 1
            break
    return res, flag


itog = 0
summa = 0
flag1 = 0
while True:
    userString = input('Введите строку чисел разделенных пробелами: ')
    summa, flag1 = f_strprocess(userString)
    itog = itog + summa
    print(f'{summa} ({itog})')
    if flag1 == 1:
        break
