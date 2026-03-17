# Q no 11

def AlphabetSoup(str):
    sorted_str = sorted(str)
    result = ""
    for ch in sorted_str:
        result += ch
    return result


str = input("Enter a string: ")
result = AlphabetSoup(str)
print("Original String:", str)
print("Alphabetical Order:", result)