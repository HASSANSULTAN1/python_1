

def perfect(number):
    if number < 1:
        return False
    
    factors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            factors_sum += i
    
    return factors_sum == number




print("  PERFECT NUMBERS BETWEEN 1 AND 1000")


for num in range(1, 1001):
    if perfect(num):
        factors = []
        for i in range(1, num):
            if num % i == 0:
                factors.append(i)
        
        factors_str = " + ".join(str(f) for f in factors)
        print(str(num) + " is a perfect number:  " + str(num) + " = " + factors_str)

