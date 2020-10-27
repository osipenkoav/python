from itertools import count
from sys import argv

if len(argv) < 2:
    print('Вызов скрипта: l4-6-1 <начальное число>')
    exit(1)

for el in count(int(argv[1])):
    if el > 15:
        break
    else:
        print(el)
