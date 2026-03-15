def count_vowels(s):
    vowels = ""
    for ch in s:
        if ch in "AEIOUaeiou":
            vowels += ch
    return len(vowels), vowels[::-1]

text = input ("enter a string :" )
count , reverse_count = count_vowels(text)
print("the vowels in string are " , count)
print("the reverse of vowels is " , reverse_count)
        

