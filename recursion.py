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



#03

def find_max(num):
  if len(num) == 1:
    return num[0]
  else:
    max_num = find_max(num[1:])
    return num [0] if num[0]>max_num else max_num
  
list_1 = [6,99,0,22,55]
print (find_max(list_1))