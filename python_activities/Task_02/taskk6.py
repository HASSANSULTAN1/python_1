

def binary2Decimal(binary):
    binary_str = str(binary)
    decimal = 0
    power = 0
    
    for digit in reversed(binary_str):
        if digit not in ('0', '1'):
            raise ValueError( "Invalid binary digit:" + str (digit))
        decimal += int(digit) * (2 ** power)
        power += 1
    
    return decimal


print(binary2Decimal(0)) 
