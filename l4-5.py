from functools import reduce

def my_f(a, b):
    return a * b

my_list = [s for s in range(100, 1001) if (s % 2 == 0)]
#print(my_list)

print(reduce(my_f, my_list))