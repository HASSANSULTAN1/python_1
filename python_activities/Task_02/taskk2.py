

def prime_factors(n):
    factors = []
    divisor = 2
    
    while divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    
    return factors

n = int(input("enter a number: "))
print("Prime factors of " + str(n) + ": " + str(prime_factors(n)))