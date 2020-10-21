def f_userout(name, family, year, city, email, tel):
    print(name, family, year, city, email, tel, sep=';')
    return 0


user1=['Carlson', 'Super', '1981', 'Oslo', 'carlson@email.ru', '2223332232233']
f_userout(name=user1[0], family=user1[1], year=user1[2], city=user1[3], email=user1[4], tel=user1[5])