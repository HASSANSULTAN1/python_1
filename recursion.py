def func_1(n):
    if n <= 10:
        print ("Hello World")
    else:
        print (n)
        func_1(n-1)    

func_1(20)                