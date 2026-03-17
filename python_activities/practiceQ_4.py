#Q n0 4

def repeat_string(s, n):
    return s * n

s = input("Enter a string: ")
n = int(input("Enter a number: "))

result = repeat_string(s, n)
print("Result:", result)