


numbers = [4, 7, 2, 9, 4, 1, 7, 3, 8, 2]


print("REMOVE DUPLICATES FROM LIST")
print("Original List (" + str(len(numbers)) + " elements):")
print(numbers)


unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("\nMethod 1 - Using Loop:")
print("Unique List (" + str(len(unique_list)) + " elements):")
print(unique_list)


set_list = list(set(numbers))
set_list.sort()

print("\nMethod 2 - Using set():")
print("Unique List (" + str(len(set_list)) + " elements):")
print(set_list)



print("\nDuplicates that were removed:")
duplicates = []
seen = []
for num in numbers:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    seen.append(num)

print(duplicates)


print("\nFrequency of each number:")

frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

for key in sorted(frequency):
    bar = "*" * frequency[key]
    print("Number " + str(key) + " : " + bar + " (appears " + str(frequency[key]) + " times)")

