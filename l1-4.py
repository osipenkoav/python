num = int(input("Enter number: "))

maxDig = 0
while num // 10 != 0:
    lastDig = num % 10
    if lastDig > maxDig:
        maxDig = lastDig
    num = num // 10

print(f'Maximum digit is: {maxDig}')
