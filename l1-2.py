userTime = int(input("Enter time in seconds: "))

hours = userTime//3600
minutes = (userTime%3600)//60
seconds = (userTime%3600)%60

print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')