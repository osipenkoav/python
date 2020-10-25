f = open('test_sotr.txt', 'r')

count_employer = 0
summa_zp = 0
for line in f:
    list_temp = line.split()
    count_employer += 1
    summa_zp = summa_zp + int(list_temp[1])
    if int(list_temp[1]) < 20000:
        print(line)
print(f'средняя ЗП: {summa_zp / count_employer}')
