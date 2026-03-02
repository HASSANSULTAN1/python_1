

# if condition in python

a=18
b=33

if b>a:
    print("Hello World")

    if a<b:
        print("WW3")


#elif in python

a = 200
b = 200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")   



score = 82

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")



#else statment in python
  
score = 44

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
else:
   print("Grade: F")



#Logical Operaters in Python
   

#AND Statment
   
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#OR Statment

a = 200
b = 33
c = 100
if a > b or c > a:
  print("Only one statment is true")   


#NOT Operator

a = 66
b = 200
if not a > b:
  print("a is not greater than b")

#using logical operators in if else statments
  
score = 85

if score >= 50 and score <= 100:
  print(" Good score")
else:
  print("Bad score")



#Nested if statments


age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("FIRRRRRR")    