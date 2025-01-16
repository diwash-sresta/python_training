numbers = [1,2,3,4,5]
# squared = list(map(lambda x:x**2, numbers))
# print(squared)

def square(x):
    return x**2
print(list(map(square,numbers)))

