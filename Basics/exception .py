# while True:
#     try:
#         x = int (input("Enter the first number"))
#         y = int (input("Enter the second number"))
#         print("Diving the numbers")
#         result = x / y
#         print(result)
#         break
#     except Exception as e :
#             print(e)

# except ZeroDivisionError:
#     print("Second number was zero")
# except ValueError:
#     print("please enter the number")

# try:
#         x = int (input("Enter the first number"))
#         y = int (input("Enter the second number"))
#         print("Diving the numbers")
#         result = x / y
#         print(result)
        
# except ZeroDivisionError :
#             print("Increase the value by 1")

# def number():
#     while True:
#         value = input("Enter a number : ")

#         try:
#             if "." in value:
#                 num = float(value)
#                 print(f"This is a float:{num}")

#             else:
#                 num = int(value)
#                 print(f"This is an integer : {num}")
#                 return num
#         except ValueError:
#             print("This is Syntax Error")

# def g_name():
#     while True:
#         name = input("Enter the name")

#         if name.isalpha():
#             return name

#         else:
#             print("Invalid input . Please enter a name consisting only letters")
#             print("Enter your first and last name : ")

# first_name = g_name()
# last_name = g_name()

# x = number()
# y = number()

# print("Dividing the numbers : ")

# if y == 0:
#     y += 1
#     print("Second num was zero. Increased the 2nd num by 1 to avoid ZeroDivisionError")
# result = x /y
# print(result)
# print(f"Hello , My name is {first_name} and my last name is {last_name}")

# x = input("Enter the number : ")
# if x.isdigit():
#     new_int = int(x)
#     print("This is integer",type(new_int))
# elif x.count(".") == 1 and x.replace(".","").isdigit():
#     new_float = float(x)
#     print(type(new_float))
# elif x.count(".")>1:
#     print("this is not float. Contains many decimal")
# else:
#     print("this is an string")

# x = input("Enter the number : ")
# try:
#     new_int = int(x)
#     print(f"This is an integer,type:{type(new_int)}")
# except ValueError:
#     try:
#         new_float = float(x)
#         print(f"this is float, type:{type(new_float)}")
#     except ValueError:
#         if x.count(".")>1:
#             print("This in not float. Contains many decimal")
#         else:
#             print("This is string")

# custom exception

# age = int(input("Enter your age : "))

# if age < 0:
#     raise Exception("Sorry , no number below zero")
# else:
#     print(age)
# /////////////////////////////////////////////

# class negative_error(Exception):
#     def __init__(self, message):
#         super().__init__(message)

# class zero_error(Exception):
#     def __init__(self, message):
#         super().__init__(message)

# x= int(input("Enter your age : "))

# try:
#     if x < 0 :
#         raise negative_error("Sorry , no number below zero")
    
#     elif x == 0:
#         raise zero_error("Sorry,age is zero")
# except negative_error as e:
#     print(e)

# ///////////////////////////////////////
# class negative_error(Exception):
#     def __init__(self, message):
#         super().__init__(message)

# class zero_error(Exception):
#     def __init__(self, message):
#         super().__init__(message)

# UI = '''        Display options:
# 1.Deposit
# 2.Withdraw
# '''
# print(UI)
# while True:
#     operations =int(input('''Press "1" to deposit and Press "2" to withdraw: '''))

#     if operations == 1:
#         deposit =int(input("Enter the amount to deposit"))
#         try:
#             if deposit <0:
#                 raise negative_error("Amount is in nagative")
#             elif deposit == 0:
#                 raise zero_error("Amount is zero")
#         except negative_error as e:
#             print(e)
#             print("You have enter negative number")
#             deposit = int(input("Enter the amount"))
#         except zero_error as e:
#             print(e)
#             print("You have enter zero")
#             deposit =int(input("Enter the amount"))

#     elif operations == 2 :
#         withdraw =int(input("Enter the amount you want to withdraw"))
#         try:
#             if withdraw <0:
#                 raise negative_error("Amount is in nagative")
#             elif withdraw == 0:
#                 raise zero_error("Amount is zero")
#         except negative_error as e:
#             print(e)
#             print("You have enter negative number")
#             deposit = int(input("Enter the amount"))
#         except zero_error as e:
#             print(e)
#             print("You have enter zero")
#             deposit =int(input("Enter the amount"))
#
 