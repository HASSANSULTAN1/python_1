#Q NO 06

def common_end(a, b):
    if a[0] == b[0] or a[-1] == b[-1]:
        return True
    return False

a = input("Enter first array: ").split()
a = [int(x) for x in a]

b = input("Enter second: ").split()
b = [int(x) for x in b]

result = common_end(a, b)
print("Array 1:", a)
print("Array 2:", b)
print("Result:", result)
