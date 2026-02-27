
# using a decorater in a function


def decorater(func):
    def wrapper():
        print("hello")
        func()
        print("good bye")
    return wrapper


@decorater
def hello():
  print('i am running in between a decorater')

hello()



def repeat(func):
    def wrapper():
        n = int(input("How many times you want to print? "))
        value = func()               
        for i in range(n):
            print(value)
    return wrapper

@repeat
def get_message():
    msg = input("Enter the message to print: ")
    return msg

get_message()


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print (list1,list2,list3)

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


