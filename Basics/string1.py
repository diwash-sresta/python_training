# s= "Hello World"
# print(s[4])
# print(s[10])
# print(s[6])
# # ///////////////slicing/////////////////////
# print(s[6:11])
# print(s[:5])
# print(s[7:])
# # ////////////skip/////////////////
# print(s[0:5:2])
# print(s[::2])
# print(len(s))
# name = "Hello World!"
# for x in range(len(name)):
#     print(name[x])
    
# name = input("Enter the string")
# count = 0

# for x in range(len(name)):
#     if name[x] =='a' or name[x]== 'e' or name[x]== 'i' or name[x]== 'o' or name[x]== 'u' :
#         count
# print("total vowel count",count)

# name = input("Enter the string:")
# count_a =0
# count_e =0
# count_i =0
# count_o =0
# count_u =0
# for x in range(len(name)):
#     if name[x]== 'a'or name[x]== "A":
#         count_a+= 1
# for x in range(len(name)):
#     if name[x]== 'e'or name[x]== "E":
#         count_e+= 1
# for x in range(len(name)):
#     if name[x]== 'i'or name[x]== "I":
#         count_i+= 1
# for x in range(len(name)):
#     if name[x]== 'o'or name[x]== "O":
#         count_o+= 1
# for x in range(len(name)):
#     if name[x]== 'u' or name[x]== "U":
#         count_u+= 1

# print("a",count_a)
# print("e",count_e)
# print("i",count_i)
# print("o",count_o)
# print("u",count_u)
# //////////////// string methods ////////////////////////
# s= "Hello"
# s= "h" + s[1:]
# print(s)

# s="Hello World"
# print(s)
# print(s.replace("World","Python"))
# print(s.replace("Hello","Bye"))

# s="HELLO WORLD"
# print(s.lower())

# s="hello world"
# print(s.upper())
# print(s.title())

# ///////////stripping///////////////////////
# s="         Hello World          "
# print(s.lstrip())
# print(s.rstrip())
# print(s.strip())

# s=["Hello , World"]
# print(s.split())
# name = " "
# print(name.join(s))

# a = 5 
# b = 10
# s= f"The sum of {a} and {b} is {a+b}"
# print(s)

# name = "####################Hello####World###############"

# s= name.strip("#")
# t=s.split("####")
# v=" "
# u =v.join(t)
# w=u.lower()
# print(w)

'''
input = "##############Hello####World############"
output = "hello world"
result = output.title().replace(" ","####")
print(result)

length_input = len(input)
# count for left trailing
left_strip = input.lstrip("#")
length_left_strip = len(left_strip)
left = length_input - length_left_strip

# count # of right trailing
right_strip = input.rstrip("#")
length_right_strip = len(right_strip)
right = length_input - length_right_strip

final_result = "#"*left + result +"#"* right
print(final_result)

'''
input = "########Hello####World#######"
output = "hello world"
result = output.title().replace(" ","####")
print(result)

length = len(input)
# calc left trailing
left_strip = input.lstrip("#")
lenght_left_strip = len(left_strip)
left = length - lenght_left_strip

#calc right traling

right_strip = input.rstrip("#")
lenght_right_strip = len(right_strip)
right = length - lenght_right_strip

Final_result = "#" * left + result + "#" * right
print(Final_result)