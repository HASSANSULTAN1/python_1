
# creating a tuple
tuple_1 = ("apple", "banana", "cherry", "apple", "cherry",100,6678,False)
print(tuple_1)

#printing through index

print(tuple_1[4],tuple_1[0])


print (len(tuple_1))

# joining tuples

tuple_2=(1,2,3)
tuple_3=("hasan","aa","bb")
tuple_4=tuple_2+tuple_3
print (tuple_4)

#update a tuple

list_1 = ("apple", "banana", "cherry")
list_2 = list(list_1)
list_2[1] = "kiwi"
list_1 = tuple(list_2)

print(list_1)