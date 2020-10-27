f = open('test_1.txt', 'r')
count_lines = 0

for line in f:
    count_lines += 1
    list_temp = line.split()
    print(f'количество слов в строке {count_lines} : {len(list_temp)}')
f.close()
print(f'количество строк в файле: {count_lines}')
