#creating a set

set_1 = {"hassan","apple",1,1000,5566}
print (set_1)

#printing length of a set

print(len(set_1))

#we cannot print a number through index because set is unordered and it does not have a index number

# frozen set
listt = frozenset({"apple", "banana", "cherry"})
print(listt)

#union in sets

set_2 = {1,2,3,4,}
set_3 = set_1.union(set_2)
print (set_3)

#loops in sets

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)




