

positive_count = 0
negative_count = 0
zero_count     = 0

while True:
    number = int(input("Enter a Number (999 to stop) : "))

    if number == 999:
        break
    elif number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

print("Positive Numbers : " + str(positive_count))
print("Negative Numbers : " + str(negative_count))
print("Zeros            : " + str(zero_count))