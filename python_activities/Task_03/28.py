


n = int(input("Enter a Number : "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
elif n == 0:
    print("Factorial of 0 is : 1")
else:
    factorial = 1
    steps     = ""

    for i in range(1, n + 1):
        factorial *= i
        steps     += str(i)
        if i != n:
            steps += " x "

    print("Factorial of " + str(n) + " = " + steps + " = " + str(factorial))