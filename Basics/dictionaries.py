# print(my_dict["name"])

# mix_dict = {
#     1 : "one",
#     2 : "two",
#     (1,2) : "tuple"

# }
# print(mix_dict.get("age","not found"))
# my_dict = {
#     "name" : "Diwash",
#     "age1" : 12,
#     "Address" : "PMR"
# }
# age2 = 10
# city = input("Enter name of your city :")

# x= my_dict["age1"]
# result = x + age2
# # print(result)
# my_dict["age1"] = result
# my_dict["Address"] = city
# print(my_dict)

# ////loop///
# thisdict = {
#     "name": "Diwash",
#     "age" : 22,
#     "Address" : "HTD"
# }
# # for x in thisdict:
# #     if x == "age":
# #         print(thisdict["age"])

# # ////items//////////
# for x ,y in thisdict.items():
#     print(x,y)

# ///////excersise///////////
# Name = input("Enter your name : ")
# Age = int(input("Enter your age : "))
# Address = input("Enter your address : ")


# info = {
# }
# while True:
#     Phone_number = input("Enter your phone number: ")
#     if len(Phone_number) == 10 and Phone_number.isdigit():
#         break
#     else:
#         print("Invalid phone number. Please enter a 10-digit number.")

# info["Name"] = Name
# info["Age"]= Age
# info["Address"] = Address
# info["Phone_number"] = Phone_number

# if Age >= 20:
#        info["Age"]+= 5

# print(info)

# ///////////// Nested dictionary ///////////
# student = {
#     "name" : "Diwash",
#     "age" : 20,
#     "grades" :{
#         "math": 50,
#         "history" : 55,
#         "science" : 60,
#         "english" : 70
#     },
#     "contact" :{
#         "email" : "asdasdas@gamil.com",
#         "phone" : 1234565897
#     }    
# }
# total = sum(student["grades"].values())
# print(total)

# ////////////////////////
student = {}

while True:
    x = input("Do you want to continue ? (y / n) :")
    if x == "n":
        break
    rollno = int(input("Enter your rollno. :"))
    name = input("Enter your name :")
    age = int(input("Enter your age :"))
    math = int(input("Enter your marks in math:"))
    history = int(input("Enter your marks in history:"))
    science = int(input("Enter your marks in science:"))
    e_mail = input("Enter your e-mail :")
    phone_no = int(input("Enter your  phone-no.:"))

    total = math + history + science

    student[rollno] = {
    "name" : name,
    "age" : age,
    "grades":{
        "math" : math,
        "history": history,
        "science": science,
    "total marks" : total    
    },
    "Contact" : {
        "e-mail" :e_mail,
        "phone_no" : phone_no
    }
}
print(student)