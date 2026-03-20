# Q # 02

def combine_vowels(arr1, arr2):
    arr3 = []
    for ch in arr1:
        if ch in "aeiouAEIOU":
            arr3.append(ch)
    for ch in arr2:
        if ch in "aeiouAEIOU":
            arr3.append(ch)
    return arr3

array1 = ['H', 'a', 's', 's', 'a', 'n']
array2 = ['S', 'u', 'l', 't', 'a', 'n']

result = combine_vowels(array1, array2)
print("Array 1:", array1)
print("Array 2:", array2)
print("Vowels combined array:", result)
print ("hi")
        

