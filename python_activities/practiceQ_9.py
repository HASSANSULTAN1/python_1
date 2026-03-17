#Q no 08

def div_by_6(s):
    count = 0
    n = len(s)
    


    for i in range(n):
        for j in range(i + 1, n + 1):
            substr = s[i:j]
            num = int(substr)
            if num % 6 == 0:
                count += 1
    
    return count


s = input("Enter a string of digits: ")
result = div_by_6(s)
print("String:", s)
print("Count of subsequences divisible by 6:", result)
