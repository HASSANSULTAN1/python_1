

def to_octal(n):
    if n == 0:
        return "0"
    
    octal = ""
    while n > 0:
        octal = str(n % 8) + octal
        n //= 8
    
    return octal

n = int(input("Enter a number: "))
print("Octal equivalent of " + str(to_octal(n)))