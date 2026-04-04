

myList = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

print("    FIRST THREE CHARACTERS OF WORDS")


print("\nOriginal List:")
print(myList)

print("\nFirst 3 Characters of each word:")



result = ""
for word in myList:
    result = result + word[:3] + " "

print(result)


print("\nWord by Word:")
for word in myList:
    print(word + "  -->  " + word[:3])





myList2 = ['January', 'February', 'March']
result2 = ""
for word in myList2:
    result2 = result2 + word[:3] + " "
print(result2)
