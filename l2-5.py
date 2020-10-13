my_list = [7, 5, 3, 3, 2]

userRating = None
while userRating != 0:
    userRating = int(input('Введите рейтинг 1-9 или 0 для выхода: '))
    if userRating == 0:
        break
    if userRating in my_list:
        my_list.insert(my_list.index(userRating) + 1, userRating)
        print(my_list)
    else:
        for i in my_list:
            if i < userRating:
                my_list.insert(my_list.index(i), userRating)
                break
            else:
                if i == my_list[-1] and i > userRating:
                    my_list.append(userRating)
        print(my_list)

print(my_list)
