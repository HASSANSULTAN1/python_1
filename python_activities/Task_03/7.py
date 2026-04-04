

number = int(input("Enter a Five Digit Number : "))

if len(str(number)) != 5:
    print("Please enter a valid 5 digit number!")
else:
    digit1 = number // 10000
    digit2 = (number % 10000) // 1000
    digit3 = (number % 1000)  // 100
    digit4 = (number % 100)   // 10
    digit5 = number % 10

    sum_digits = digit1 + digit2 + digit3 + digit4 + digit5

    print("Digits     : " + str(digit1) + " " + str(digit2) + " " + str(digit3) + " " + str(digit4) + " " + str(digit5))
    print("Sum        : " + str(sum_digits))
