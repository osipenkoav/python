def my_func(a1, a2):
    try:
        res = a1 / a2
    except:
        print('Деление на ноль!')
        return 0
    return res


print('Результат деления число1/число2:', my_func(int(input('Введите число1: ')), int(input('Введите число2: '))))
