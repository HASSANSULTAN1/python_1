import random


numbers = [random.randint(1, 100) for i in range(10)]


print("     MEAN, MEDIAN AND MODE")
print("List of 10 Random Integers:")
print(numbers)


total = 0
for num in numbers:
    total += num
mean = total / len(numbers)
print("Mean   : " + str(mean))


sorted_nums = sorted(numbers)
n = len(sorted_nums)
if n % 2 == 0:
    median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
else:
    median = sorted_nums[n//2]
print("Median : " + str(median))


frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_freq = max(frequency.values())
if max_freq == 1:
    print("Mode   : No unique mode (all values appear once)")
else:
    modes = []
    for key in frequency:
        if frequency[key] == max_freq:
            modes.append(key)
    print("Mode   : " + str(modes))


print("Sorted List : " + str(sorted_nums))
print("Frequency   : " + str(frequency))
