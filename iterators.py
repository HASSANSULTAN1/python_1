#learning iterators

tuple_1 = ("apple", "yokohama", "hassan")
myit = iter(tuple_1)

print(next(myit))
print(next(myit))
print(next(myit))


#iterating in a string

mystr = "yayayaya"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


import datetime

x = datetime.datetime.now()
print(x)