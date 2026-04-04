



num1 = int(input("Enter First Integer  : "))
num2 = int(input("Enter Second Integer : "))
num3 = int(input("Enter Third Integer  : "))

sum_nums     = num1 + num2 + num3
average      = sum_nums / 3
product      = num1 * num2 * num3


if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3


if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("Sum is      " + str(sum_nums))
print("Average is  " + str(average))
print("Product is  " + str(product))
print("Smallest is " + str(smallest))
print("Largest is  " + str(largest))