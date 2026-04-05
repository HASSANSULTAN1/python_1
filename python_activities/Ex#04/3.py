



n = int(input("Enter number of elements: "))

original = []
for i in range(n):
    val = int(input("Enter element " + str(i + 1) + ": "))
    original.append(val)

k = int(input("Enter rotation steps: "))

print("Original Array : " + str(original))

k = k % n 
rotated = original[n - k:] + original[:n - k]
print("Rotated Array  : " + str(rotated))

combined = original + rotated
print("Combined Array : " + str(combined))

min_val   = combined[0]

for i in range(1, len(combined)):
    if combined[i] < min_val:
        min_val   = combined[i]
        min_index = i

print("Minimum Value  : " + str(min_val))