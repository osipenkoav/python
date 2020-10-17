def my_func_simple(x, y):
    return x ** y


def my_func(x, y):
    y = abs(y)
    res = 1
    for i in range(y):
        res = res * 1 / x
    return res


print('Результат x в степени -y: ', my_func(float(input('Введите основание: ')), int(input('Введите минус степень: '))))
print('*' * 10)
print('Результат x в степени -y: ',
      my_func_simple(float(input('Введите основание: ')), int(input('Введите минус степень: '))))
