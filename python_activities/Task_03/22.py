


total    = 0
even_nums = []

for i in range(2, 31, 2):
    total += i
    even_nums.append(i)

print("Even Numbers : " + str(even_nums))
print("Sum          : " + str(total))