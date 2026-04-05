

n = int(input("Enter a Number: "))

squares_dict = {}
for i in range(1, n + 1):
    squares_dict[i] = i * i

print(squares_dict)