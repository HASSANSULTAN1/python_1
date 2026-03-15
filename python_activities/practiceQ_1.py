def count_and_reverse_vowels(s):
    vowels = ""
    for ch in s:
        if ch in "aeiouAEIOU":
            vowels += ch
    return len(vowels), vowels[::-1]


text = input('enter a string : ')
count, reversed_vowels = count_and_reverse_vowels(text)
print("Vowel count:", count)
print("Vowels in reverse:", reversed_vowels)