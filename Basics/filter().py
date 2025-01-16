numbers = [1,2,3,4,5,6,7]
even_numbers = list(filter(lambda x :x%2 == 0,numbers))
print(even_numbers)

def even(x):
    if x %2 == 0:
        return x
even = list(filter(even,numbers))

    