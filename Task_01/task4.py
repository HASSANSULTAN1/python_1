#4.	Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return thrice of their sum

num1 = int(input("Enter 1 num: "))
num2 = int(input("Enter 2 num: "))
num3 = int(input("Enter 3 num: "))

result = num1 + num2 + num3 

if num1 == num2 == num3:
    print(result * 3)
else:
    print(result)    