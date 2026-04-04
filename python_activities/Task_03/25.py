


numbers = []
while True:
    num = int(input("Enter a Number (999 to stop) : "))
    if num == 999:
        break
    numbers.append(num)

if len(numbers) == 0:
    print("No numbers entered.")
else:
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num

    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    range_val = largest - smallest

    print("Numbers  : " + str(numbers))
    print("Smallest : " + str(smallest))
    print("Largest  : " + str(largest))
    print("Range    : " + str(range_val))