revenue = int(input("Input your revenue: "))
cost = int(input("Input your cost: "))

if revenue > cost:
    print("You have profit!")
    print(f'Your efficiency is: {(revenue - cost) / revenue : 05.2f}')
    numStaff = int(input("How many employees you have? "))
    print(f'For one employeer you have {(revenue - cost) / numStaff : 05.2f} profit')
else:
    print("You have loss...")
