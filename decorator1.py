# without parameter 
# def decorator2(x):
#     def wrapper():
#         print("something before functions runs")
#         print("start time")
#         x()
#         print("endtime - starttime")
#     return wrapper

# @decorator2
# def say_hello():
#     print("Hello")

# say_hello()

# def say_goodgye():
#     print("Good Bye")
# say_goodgye()

# with parameter

# def decorator3(fun):
#     def wrapper(*args,**kwargs):
#         print("something before functions run")
#         result = fun(*args,**kwargs)
#         print("After the function call")
#         return result
#     return wrapper

# @decorator3
# def say_hello(name, greeting = "Hello"):
#     print(f"{greeting},{name}!")

# say_hello("Alice")
# say_hello("Boby", greeting="Namaste")

def great_decorator(greetings):
    def decorator4(fun):
        def wrapper (*args,**kwargs):
            print(f"{greetings} before functions runs")

            fun(*args,**kwargs)
            print("Something after the functions runs")
        return wrapper
    return decorator4

@great_decorator("Hello")
def say_hello(name,greeting = "Hi"):
    print(f"{greeting},{name} ")
say_hello("Diwash")