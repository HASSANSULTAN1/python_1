

year = int(input("Enter Year : "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(str(year) + " is a Leap Year.")
else:
    print(str(year) + " is NOT a Leap Year.")