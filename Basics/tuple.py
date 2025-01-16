# tup = ()
# even = [i for i in range(1,11) if i%2==0]
# tup = tuple(even)
# print(tup)

# ///////unpaking tuple///////////////
# tuple1 = (1,2,3,4,5,"abc","bye","Hi")
# a,b,c,d,*z = tuple1
# print(a)
# print(b)
# print(c)
# print(d)
# print(z)

numbers = [(2,3),(4,5),(6,7),(8,9),(0,0),(6,6)]
sum_num = []
for num in numbers:
    for x in num:
        sum_num = sum(num)
    print(f"{num} sum is {sum_num}")
max_num = max(numbers)
sum_max = sum(max_num)
print(f"The maximum number is of combination{max_num} is {sum_max}")

num = [1,4,5,7,9,-1,100,-35,1000]
max_num = max(num)
print(f"The maximum number is {max_num}")
