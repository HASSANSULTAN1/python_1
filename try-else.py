#try , except


try:
    print(x)
except:
    print("x is not defined")   


#try , except , else

try:
    ("print hello")

except:
    ("something went wrong")

else:
    print("everything is all right")  

#try , except , else , finally 

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("it skips the try-except part")             