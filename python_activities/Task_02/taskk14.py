


def find_minimum(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num



numbers = (45, 72, 23, 88, 12, 67, 34, 90, 56, 38)

print("FIND MINIMUM IN A TUPLE")
print("Tuple of 10 Numbers:")
print(numbers)


minimum = find_minimum(numbers)
print("Minimum Number : " + str(minimum))






tuple1 = (5, 3, 8, 1, 9, 2, 7, 4, 6, 10)
tuple2 = (100, 200, 300, 400, 500, 600, 700, 800, 900, 1000)
tuple3 = (-5, -3, -8, -1, -9, -2, -7, -4, -6, -10)
tuple4 = (15, 15, 15, 15, 10, 15, 15, 15, 15, 15)

print("Tuple 1 : " + str(tuple1))
print("Minimum : " + str(find_minimum(tuple1)))


print("Tuple 2 : " + str(tuple2))
print("Minimum : " + str(find_minimum(tuple2)))


print("Tuple 3 : " + str(tuple3))
print("Minimum : " + str(find_minimum(tuple3)))


print("Tuple 4 : " + str(tuple4))
print("Minimum : " + str(find_minimum(tuple4)))
