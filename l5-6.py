f = open('test6.txt', 'r')
dict_res = {}

for line in f:
    list_temp = line.split()
    count_hours = 0
    for i in list_temp:
        if i.find(':') != -1:
            name_subj = i[:-1]
            continue
        if i.find('-') != -1:
            continue
        if i.find('(') != -1:
            count_hours = count_hours + int(i[:i.find('(')])
    dict_res[name_subj] = count_hours
print(str(dict_res))

f.close()
