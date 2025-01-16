# x = lambda a : 10/a
# print(x(5))

# x = lambda a,b,c : a*b*c
# print(x(2,2,2))

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(1010))