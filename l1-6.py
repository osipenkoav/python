a = int(input("Enter kilometers for 1-st day: "))
b = int(input("Enter target kilometers: "))

countDay = 1
while a < b:
    countDay += 1
    a = a * 1.1

print(f'for day {countDay} result will be {a : 5.2f} kilometrs')
