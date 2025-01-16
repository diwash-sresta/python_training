#  ////////checking data types /////////////
# # x ='5' 
# # print (type(x))
 # #  y = "hello"
# print(type(y))
# x=20.5
# print(type(x))
 # x=1j
 # print(type(x))
 # x=["apple","banana","cherry"]
 # print(type(x))
 # x= ("apple","banana","cat")
 # print(type(x))
 # x=range(6)
 # print(type(x))
 # x={"name": "john","age":20}
 # print(type(x))
 # x= {"apple","banana","cat"}
 # print(type(x))
 # x= frozenset({'apple','banana','cat'})
 # print(type(x))
 # x=True
 # print(type(x))
 # x= None
 # print(type(x))
 # #condtional
 # a= int(input("Enter number of a"))
 # b= int(input("Enter number of b"))
 # if b != a:
 #     print("a is not equal than to b")
 #////checking number is positive ,negative ,zero/////////////
 # #pos = "number is positive"
 # #neg ="nunmber is negative"2
 # # #zero ="number is zero"
 # a = int(input("Enter the number of a"))
 # if a > 0:
 #     print("a is positive")
 # elif a<0:
 #     print("a is negative")
 # elif a==0:
 #     print("a is zero")
 #////checking odd or even///////
 # number = int(input("enter the number "))
 # if number%2 == 0:
 #     print("number is even")
 # elif number%2!=0:
 #     print("number is odd")
 #///for and while loop///////
 # # numbers = ['a','b','c','d']
 # # for num in numbers:
 # #     print(num)
 # # for x in range (2,7):
 # #     print(x)
 # # for x in range (2,8,3):
 # #     print(x)
 # # numbers = [1,2,3,4,5,6]
 # # for num in range(4):
 # #     print(num)
 # # mixed = ["hello",1,2,6,[3,5],True,None]
 # # for x in mixed:
 # #     print(x)
# # # #     if type == str:
# # # #         print(f"it is string{x}")
# # # #     elif type(x) ==int:
# # # #         print

# # # # using range get even and odd of range(1,100)

# # # # Numbers = [1,100]
# # # # for num in range(1,100,2):
# # #  #     print("even number")
# # # #     print(num)

# # # # Numbers = [1,100]
# # # # for num in range(2,100,2):
# # #  #   print("odd number")
# # # #     print(num)
        

# # # for x in range(1,10):
# # #     if x%2==0:
# # #         print("skip")
# # #         continue
# # #     elif x%2 != 0:
# # #         print(x)

# # i=0
# # while i<10:
# #     if i%2==0:
# #         i+=1
# #         print("skip")

# #         continue
# #     print(i)
# #     i+=1


   
#     # swapping variable

# # x,y = 10 ,20
# # x,y = y,x
# # print(x,y)

# x=10
# y = 20
# temp = x
# x=y
# y= temp
# print(x,y)

# ////////////using for and while loop//////////////
# 1
# 1 2
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5 

# ////////////using for loop////////////////
# n= int(input("Enter the number of rows:"))
# for i in range (1,n+1):
#     for j in range(1, i+1):
#         print(j,end="")
#     print()
# ////using while////////////////////////
i=1
while i<=5:
    j=1
    while j<=i:
        print(j ,end="")
        j+=1
    i+=1
    print()
    
