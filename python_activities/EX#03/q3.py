


words = input("Enter words: ")

word_list = words.split(",")
word_list.sort()
result = ",".join(word_list)


print(result)