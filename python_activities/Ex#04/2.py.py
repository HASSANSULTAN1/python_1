


def count_ones(n):
    count = 0
    for i in range(1, n + 1):
        for digit in str(i):
            if digit == '1':
                count += 1
    return count


n = int(input("Enter a number n: "))

result = count_ones(n)

numbers_with_one = []
for i in range(1, n + 1):
    if '1' in str(i):
        numbers_with_one.append(i)

print("Numbers containing digit 1 : " + str(numbers_with_one))
print("Total count of digit 1     : " + str(result))