#01

def func_1(n):
    if n <= 10:
        print ("Hello World")
    else:
        print (n)
        func_1(n-1)    

func_1(20)  

#02

def fac_01(n):
    if n <= 1 :
        return n
    else:
          return n * fac_01(n-1)


print (fac_01(20))