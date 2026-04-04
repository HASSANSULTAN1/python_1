


num1 = float(input("Enter First Number  : "))
num2 = float(input("Enter Second Number : "))

print("Sum        : " + str(num1 + num2))
print("Product    : " + str(num1 * num2))
print("Difference : " + str(num1 - num2))
if num2 != 0:
    print("Quotient   : " + str(num1 / num2))
    print("Remainder  : " + str(num1 % num2))
else:
    print("Quotient   : Cannot divide by zero")
    print("Remainder  : Cannot divide by zero")