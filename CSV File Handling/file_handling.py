# f = open("demofile.txt","r")
# value = f.read()
# print(type(f.read()))

# # output = []
# # for s in value.split():
# #     if s in ["Hello","testing","Good"]:
# #        print(s)
# print(value[:5])
# print(value[-27:-20])
# f.close()

# f = open("demofile.txt","r")
# value = f.readlines()
# new_list = [x.strip("\n" )for x in value]
# # for x in value:
# #     print(x.strip())
# print(new_list)
# f.close()

# file_path = "demofile.txt"
# with open(file_path,"r")as file:
#     content = file.read()
#     print(content)

# f = open("demofile.txt" ,"a")
# f.write(input("\nEnter the content you want to add"))
# f.close()

# f = open("demofile.txt","r")
# print(f.read()) 