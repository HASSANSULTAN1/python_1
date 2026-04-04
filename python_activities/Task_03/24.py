


number = int(input("Enter a Number : "))

if number == 0:
    print("Binary Equivalent : 0")
else:
    original = number
    binary   = ""

    while number > 0:
        remainder = number % 2
        binary    = str(remainder) + binary
        number    = number // 2

    print("Binary Equivalent of " + str(original) + " is : " + binary)