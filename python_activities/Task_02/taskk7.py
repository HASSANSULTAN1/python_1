

def Multiple(a, b):
    if a == 0:
        raise ValueError("First number cannot be zero")
    return b % a == 0

print(Multiple(6, 15))
print(Multiple(7, 14)) 