f = open('test_4.txt', 'r')
dict_translate = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

f_w = open('test4_new.txt', 'w')

for line in f:
    list_temp = line.split()
    list_temp[0] = dict_translate[list_temp[0]]
    # print(list_temp[0])
    f_w.write(' '.join(list_temp) + '\n')

f.close()
f_w.close()
