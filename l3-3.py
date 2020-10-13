def f_summax(a1, a2, a3):
    list1 = [a1, a2, a3]
    list1.pop(list1.index(min(list1)))
    return list1[0] + list1[1]


print('Сумма двух наибольших: ',
      f_summax(int(input('Введите число1: ')), int(input('Введите число2: ')), int(input('Введите число3: '))))
