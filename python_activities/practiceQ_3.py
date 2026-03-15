def third_and_largest(arr):
    arr = sorted(arr, reverse=True)
    largest = arr[0]
    third = arr[2]
    return largest, third

arr = input("Enter numbers: ").split() 
arr = [int(x) for x in arr]

largest, third = third_and_largest(arr)
print("Array:", arr)
print("Largest Number:", largest)
print("3rd Largest Number:", third)