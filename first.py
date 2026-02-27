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

