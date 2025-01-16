# numbers = [1,2,3,4,5]

# fruits = ["apple","banana", "cherry","Apple","APple","APPle","APPLe","APPLE"]

# mixed_list = [10 , "hello",True,1,3.14]

# print(numbers[2])
# print(fruits[-1])
# print(mixed_list[2])
# # sum = 0
# # for x in numbers:
    
# #     sum  = sum+x 
# #     print(sum)
# # print(sum)
# print(sum(numbers))



# for f in fruits:
#     if f == "apple" or f =="Apple" or f=="APple" or f=="APPle" or f=="APPLe" or f=="APPLE":
#     # if f.lower() == "apple"
#         print(f)
    
# for m in mixed_list:
#     if m == True:
#         print(m)
# sum = 0
# for a in mixed_list:
#     if type(a) == int or type(a) == float:
#         sum = sum + a
#         print(sum)
# print(sum)

# print(numbers[0:5:2])
# '''for reverse list'''
# print(numbers[::-1])  

# fruit_list =["apple","banana","cherry","kiwi","mango"]
# fruit_list[2] = "carrot"
# print(fruit_list)

# fruit_list =["apple","banana","cherry","kiwi","mango"]
# fruit_list[1:3] = ["asdsd","qweqwe"]
# print(fruit_list)

# thislist = ["apple","banana","cherry"]
# thislist.insert(2,"mango")
# thislist.append("orange")

# print(thislist)

# fruit_basket = []
# for x in range(6):
#     fruit = input("Enter the name of the fruit :")
#     fruit_basket.append(fruit)
#     print(fruit_basket)

# list = []
# while True:
#     num = int(input("Enter the number :"))
#     if num == 5:
#         break
#     list.append(num)
# print(list)
# print("list_sum",sum(list))
    
# input = input("Enter the word :")

# if input == input[::-1]:
#         print("Palindrome")
# else :
#         print("NOt palindrome")

# thislist = ["apple","banana","cherry","Apple","APple","BALL","Cat","asD"]
# addlist = [1,2,24,4,54]
# thislist.remove("banana")
# thislist.clear()
# thislist.pop(2)
# del thislist[1:]
# addlist.extend(thislist)

# thislist.sort()
# addlist.sort(reverse = True)
# print(thislist)
# print(addlist)

# thislist = ["apple","banana","cherry"]
# mylist = thislist.copy() //deep copy
# mylist = list(thislist) //direct copy
# mylist = thislist[:] // slice copy
# print(mylist)
# print(thislist)

# ////////////join list//////////
# list1 = ['a','b', 'c']
# list2 = [1,2,3]
# list3 = list1+list2
# print(list3)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# sum = 0
# for x in matrix:
#     for a in x:
#         if a == 1 or a == 5 or a==9:
#             sum = sum +a
#             print(sum)

# print(matrix[0][0])
# print(matrix[1][1])
# print(matrix[2][2])

# result = 0
# for x in matrix:
#     result = result + sum(x)
#     # final_result =sum(result)
# print(result)

# lst = [1,1,2,2,3,3,3,4,4,4,5,5,5,5,2,2,2,2,2,6,6,6,6,9,7,8]
# output = [1,2,6,7,8]

# output = []

# for x in lst:
#     if x not in output:
#         output.append(x)
# print(output)

# for x in lst:
#     if lst.count(x)>1:
#         lst.remove(x)
# print(lst)

# for x in lst:
#     if  lst.count(x) <= 2  and x not in output:
#          output.append(x)
    
# print(output)
# using a for loop
squares = []
for i in range(1,6):
    squares.append(i**2)
print(squares)

#  using list comprehension
squares = [i**2 for i in range(1,11)]
print(squares)
even = [i for i in range(1,11) if i%2==0]
total_sum = sum([i for i in range(1,11) if i%2==0])
even_odd = ["even" if i%2==0 else "odd "for i in range(1,11) ]
print(even)
print(total_sum)
print(even_odd)