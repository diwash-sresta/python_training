# Palindrome
"""
def check_palindrome(text):
    return text == text[::-1]

int = input("Enter the text to check paloindrome : ")
if check_palindrome(int):
    print("True")
else:
    print("False")
    """

# Area of circle
'''
pi = 3.14
def area_circle(radius):
    area = pi*radius*radius
    return area
int_radius = int(input("Enter the radius of circle: "))
result = area_circle(int_radius)
print(result)

'''
# Check primenumber
'''
fac = 0
n = int(input("Enter the number : "))
for x in range(1,n+1):
    if n%x == 0:
        fac = fac +1
if fac == 2:
    print("Prime number")
else:
    print("Not prime number")
   
 '''
# Fibonacci sequence

# simple interest calculator
'''
def simple_interest_calc(p,t,r):
     interest = (p*t*r)/100
     return interest
p = int(input("Enter the amount of the principle : "))
t = int(input("Entet the time in years : "))
r = int(input("Entet the rate (%) : "))

result = simple_interest_calc(p,t,r)
print(f"The interest of Nrs.{p} of {r}%rate in {t}years is {result}")
'''
# Multiplication table
'''
int = int(input("Enter the number : "))
for x in range(1,11):
    result = int * x
    print(f"{int} * {x} = {result}" )

'''
# check leap year
'''
year = int(input("Enter the years : "))

if year%4 ==0:
    print("leap year")
else:
    print("not leap year")
'''
# count vowel
'''
count = 0
int_str = input("Enter the string to check vowel : ")
for x in int_str:
    if x == "a" or x == "e"  or x == "i" or x == "o"  or x == "u":
        count+=1
print(count)
'''

        