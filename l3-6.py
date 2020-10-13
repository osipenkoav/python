def int_func(s1):
    return s1.capitalize()


def ss_int_func(ss):
    res = []
    list1 = ss.split()
    for i in list1:
        res.append(int_func(i))
    return ' '.join(res)


print(int_func('text'))
print(ss_int_func('dfdfdf  rrrttrt  nvnvn xxx   qqqq  r g g g g'))
