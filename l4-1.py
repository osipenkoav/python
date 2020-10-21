from sys import argv


def f_zp(hours, rate, gain):
    return hours * rate + gain


if len(argv) < 4:
    print('Вызов скрипта: l4-1 <выработка, час> <ставка, руб/час> <премия, руб>')
    exit(1)

script_name, first_param, second_param, third_param = argv
print('Рассчитанная зарплата: ', f_zp(int(first_param), int(second_param), int(third_param)))
