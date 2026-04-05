

num1 = int(input("Enter First Integer  : "))
num2 = int(input("Enter Second Integer : "))

if num2 == 0:
    print("Cannot divide by zero.")
elif num1 % num2 == 0:
    print(str(num1) + " IS a multiple of " + str(num2))
else:
    print(str(num1) + " is NOT a multiple of " + str(num2))