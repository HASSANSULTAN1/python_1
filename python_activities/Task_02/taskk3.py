


def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n

n = int(input("Enter a number: "))

if is_armstrong(n):
    print( str(n) + "is an Armstrong number")
else:
    print(str(n) + " is not an Armstrong number")