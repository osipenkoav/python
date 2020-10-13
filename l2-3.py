list_winter = [1, 2, 12]
list_spring = [3, 4, 5]
list_summer = [6, 7, 8]
list_autumn = [9, 10, 11]

userMounth = int(input('Введите месяц 1-12: '))

if userMounth in list_winter:
    print('Зима')
if userMounth in list_spring:
    print('Весна')
if userMounth in list_summer:
    print('Лето')
if userMounth in list_autumn:
    print('Осень')

dict_mounth = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень',
               10: 'Осень', 11: 'Осень', 12: 'Зима'}
print('Значение времени года из словаря:', dict_mounth[userMounth])
