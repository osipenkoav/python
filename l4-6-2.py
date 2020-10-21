from itertools import cycle
from sys import argv

if len(argv) < 2:
    print('Вызов скрипта: l4-6-2 <набор букв> \nПример: l4-6-2 ABC')
    exit(1)

с = 0
for el in cycle(argv[1]):
    if с > 10:
        break
    print(el)
    с += 1
