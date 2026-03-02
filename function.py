

#fiunctions in python

#Calling a function

def function_1():
    print("Hello World")

function_1()  

#function is returning a  value

def function_2():
    return("YAYAYA")

print(function_2())



#Arguments in function

def average(marks, totalmarks):
    print((marks * 100) / totalmarks)

average(50, 100)


def my_function(name):
  print("Hello", name)

my_function("Hassan")


#args in python   // we use args when we don't know how many arguments are we going to pass (tuples)

def function_5(*names):
    print("Hello",names)

function_5("hassan","ibi","zoro")  


#example 2

def function_6(message,*names):
    print(message,names)

function_6("good morning","hassan","ibi","zoro")


#kwargs in python  (it take in a dictionary)

def function_7(**var):
  print("Name:", var["name"])
  print("Age:", var["age"])
  print("All data:", var)

function_7(name = "Hassan", age = 22, city = "Lahore")


#combining args and kwargs

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Hassan", "Zoro", age = 22, city = "Islamabad")
    
    

