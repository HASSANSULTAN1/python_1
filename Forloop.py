

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)



 #break statment in for loops

  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 


#range in for loops

for x in range(2,6):     #print the number in bewteen the given numbers range
  print(x)


for x in range(2, 30, 3):  #the third number identifies the size of increment
  print(x)  

#Nested if loops

colors = ["red", "yellow", "purple"]
fruits = ["apple", "banana", "cherry"]

for x in colors:
  for y in fruits:
    print(x, y) 