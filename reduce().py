from functools import reduce

numbers = [1,2,3,4,5]
sum = reduce(lambda x,y: x + y ,numbers)
max = reduce(lambda x ,y : x if x > y else y ,numbers)
product = reduce(lambda x ,y : x * y ,numbers)
print(sum)
print(max)
print(product)

words = ["Hello","","World","!"]
sentence = reduce(lambda x ,y : x + y ,words)
print(sentence)