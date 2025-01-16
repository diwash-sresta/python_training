# ////// parameter less function/////////////
'''
def add():
    print("adding")
print("Entering a function")
add()

'''
# /// parameter less with return ////////
'''
def add ():
    print("adding")
    return "abc"
print("entering the function")
x = add()
print(x)

'''

# ////with parameter //////////////
'''
def add(a,b):
    print("adding")
    result = a + b
    print(result)
print("Entering a function")
a = 1
b = 3
add(a,b)

'''
# ///// parameter with return ////////
'''
def add(x,y):
    print("adding")
    result = x + y
    return result
print("ENterring a fuinctiopn")
a = 1 
b = 2
addintion = add(a,b)

final_result = addintion + 10
print (final_result)

'''
# //////////////////////
'''
def get_stats(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    sum_value = sum(numbers)
    return (min_value, max_value , sum_value)

# calling function
'''
# numbers = [1,2,3,4,5]
# min_val,max_val, total_sum = get_stats(numbers)

# print("Minimum",min_val)
# print("Maximum", max_val)
# print("Sum",total_sum)

'''
numbers = [1,2,3,4,5]
result = get_stats(numbers)


print("Minimum",result[0])
print("Maximum", result[1])
print("Sum",result[2])

'''

# /////default argument ////////
'''
def add (x,z,a =1):
    print("adding")
    result = x + z
    name = "abc"
    return result
x = add(1,2,2)
print(x)
'''
# //////////    Calculator       //////////////////////////
def add(x,y):
    print("addition")
    a = x + y
    return a
# def sub(x,y):
#     print("subtraction")
#     s = x - y
#     return s
# def mul(x,y):
#     print("multiplication")
#     m = x * y
#     return m
# def div(x,y):
#     print("divisoin")
#     d = x / y
#     return d
# def expo(x,y):
#     print("exponential")
#     e = x ** y
#     return e
# def f_div(x,y):
#     print("floor division")
#     fd = x // y
#     return fd
# def mod(x,y):
#     print("modulus")
#     md = x % y
#     return md

# UI = '''    display options  :  
# 1.add   
# 2.substraction  
# 3.multiplication
# 4.division  
# 5.exponential   
# 6.floor division   
# 7.modulus
# 8.exit  '''
# print (UI)

# while True:
#     operation = int(input("Select the  opertaion you want to perfrom :"))
    
#     if operation == 8:
#         print("Exiting the program")
#         break

#     n1 = int(input("Enter the first number :"))
#     n2 = int(input("Enter the second number :"))


#     if operation == 1:
#         result = add(n1,n2)
#         print(result)

#     elif operation == 2:
#         result = sub(n1,n2)
#         print(result)
    
#     elif operation == 3:
#         result = mul(n1,n2)
#         print(result)

#     elif operation == 4:
#         result = div(n1,n2)
#         print(result)

#     elif operation == 5:
#         result = expo(n1,n2)
#         print(result)

#     elif operation == 6:
#         result = f_div(n1,n2)
#         print(result)

#     elif operation == 7:
#         result = mod(n1,n2)
#         print(result)

# ////////// local and global variable////////////////
# local variable
# def my_function():
#     x = 10
#     print("Inside function:",x)

# my_function()
# print("outside function:",x) #x not defined 

# global variable
'''
y = 20

def my_function():
    print("Inside function:" ,y)

my_function()
print("Outside function",y)

'''
'''
z = 30 

def update_global():
    global z 
    z = z + 5
    print("Inside function",z)

update_global()
print("Outside function",z)

'''
# ////////// args /////////////////

# def my_function(*kids):
#     for x in kids:
#             print(x)

# my_function("Emil","Tobias","Linus")

# def my_function(**kid):
#     print("His last name is " + kid["lname"])
# my_function(fname = "Ram" , lname = "Hari")

# /// using *args and **kwargs  ///////////

# def my_function(*args,**kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# my_function("apple","banana", fruit = "cherry" ,price = 1.99)

# recursive function

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n-1)

final_result = fact(5)
print("final_result",final_result)

# palindrome

# def is_palindrome(input_string):
#     result = "".join(input_string.split()).lower()
#     return result == result[::-1]

# input_string = input("Enter the string to check palindrome : ")
# if is_palindrome(input_string):
#     print("It is palindrome")
# else:
#     print("It in not a palindrome")
