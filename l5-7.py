import json

dict_firms = {}
dict_avg = {}

with open('test7.txt', 'r') as f:
    summa_profit = 0
    count_profit_firms = 0
    for line in f:
        list_temp = line.split()
        print(list_temp)
        if (int(list_temp[2]) - int(list_temp[3])) > 0:
            count_profit_firms += 1
            summa_profit += int(list_temp[2]) - int(list_temp[3])
        dict_firms[list_temp[0]] = int(list_temp[2]) - int(list_temp[3])
    dict_avg['average_profit'] = summa_profit / count_profit_firms

list_res = []
list_res.append(dict_firms)
list_res.append(dict_avg)

with open('test7_new.txt', 'w') as f:
    f.write(json.dumps(list_res))
