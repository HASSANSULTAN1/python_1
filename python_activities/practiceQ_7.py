#Q NO 07

def lone_sum(a, b, c):
    total = 0
    if a != b and a != c:
        total += a
    if b != a and b != c:
        total += b
    if c != a and c != b:
        total += c
    return total

# Take input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

result = lone_sum(a, b, c)
print("Result:", result)