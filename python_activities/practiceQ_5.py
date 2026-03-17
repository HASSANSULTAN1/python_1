# Q 05

def array(arr):
    for i in range(len(arr) - 2):
        if arr[i] == 1 and arr[i+1] == 2 and arr[i+2] == 3:
            return True
    return False

arr = input("Enter numbers ").split()
arr = [int(x) for x in arr]

result = array(arr)
print("Array:", arr)
print("Result:", result)