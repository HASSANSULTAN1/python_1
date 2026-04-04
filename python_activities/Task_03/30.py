


side = int(input("Enter Side of Square (1-20): "))

if side < 1 or side > 20:
    print("Please enter a size between 1 and 20.")
else:
    for i in range(side):
        print("*" * side)

