# Task # 01
"""""
def repeat(func):
    def wrapper():
        m = input("What do you want to print? ")  
        n = int(input("How many times do you want to print? "))  
        
        i = 0
        while i < n:       
            print(m)
            i += 1         

    return wrapper

@repeat
def call():                
    pass

call()



#Task no 02
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"The function {func.__name__} took {end - start:.4f} seconds to execute")
        return result
    return wrapper  

@timer
def func_100():
    print("I am a function")

func_100()
"""

#Task no 03

def upper(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        print(result.upper())
    return wrapper

@upper
def func_200():
    text = input ( "What u want to print ")
    return text

func_200()


