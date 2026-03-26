#6.	Write a Python program to count the number 4 in a given list.

numbers = list(map(int, input("Enter numbers: ").split(",")))
count = 0
for n in numbers:
  if n == 4:
   count += 1


print(count)