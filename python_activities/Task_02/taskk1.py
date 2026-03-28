


def is_substring_of_either():
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    return s1 in s2 or s2 in s1

result = is_substring_of_either()
print(result)