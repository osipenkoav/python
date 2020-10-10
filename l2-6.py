list_res = []
print('Ввод товаров:')

userMenu = None
count = 0
while userMenu != 0:
    userMenu = int(input('Добавть товар? [1 - да, 0 - нет]: '))
    if userMenu == 0:
        break
    elif userMenu != 1:
        continue
    userName = input('Название товара: ')
    userPrice = input('Цена: ')
    userCount = input('Количество: ')
    userMetric = input('Единица измерения: ')
    list_res.append((count, {'Название': userName, 'Цена': userPrice, 'Количество': userCount, 'Ед': userMetric}))
    count += 1
    print('товар добавлен')

#print(list_res)

dict_res = {'Название': [], 'Цена': [], 'Количество': [], 'Ед': []}
for i in list_res:
    dict_res['Название'].append(i[1]['Название'])
    dict_res['Цена'].append(i[1]['Цена'])
    dict_res['Количество'].append(i[1]['Количество'])
    dict_res['Ед'].append(i[1]['Ед'])

print(dict_res)
