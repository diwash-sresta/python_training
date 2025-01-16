import csv
UI = input('''Press "1" to add student record & Press "2" to search stundent record :''')
file_path = "reportcard.csv"
if UI == "1":
   while True:
       name = input("Enter the name : ")
       science= int(input("Enter the marks in science : "))
       history= int(input("Enter the marks in history : "))
       english= int(input("Enter the marks in english : "))
       total = science + history + english    
       data = [
           [name,science,history,english,total]
        ]
       
       with open(file_path,mode = "a", newline="")as file:
           csv_writer = csv.writer(file)
           # csv_writer.writerow(["Name","science","history","english","total"])
           for row in data:
               csv_writer.writerow(row)
       cont = input("Do you want to add another record? (Y/N)")
       if cont!="y":
            break
elif UI == "2":        
    
    search = input("Enter the name of the student record you want : ") 
    found = False    
    with open(file_path,mode = "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row and row[0].lower() == search.lower():
                print(f"Record found : {row}")
                found = True
                break
    if not found:
        print(f"No student record for student : {search}")

else:
    print("Invalid input. Press '1' or Press '2' ")

# //// enhanced code with Chatgpt /////////////////
# import csv

# UI = input('''Press "1" to add student record & Press "2" to search student record: ''')
# file_path = "reportcard.csv"

# if UI == "1":
#     while True:
#         # Collect student information
#         name = input("Enter the name: ")
#         science = int(input("Enter the marks in science: "))
#         history = int(input("Enter the marks in history: "))
#         english = int(input("Enter the marks in English: "))
#         total = science + history + english

#         # Write to CSV
#         with open(file_path, mode="a", newline="") as file:
#             csv_writer = csv.writer(file)
#             # Write header only if the file is empty
#             if file.tell() == 0:
#                 csv_writer.writerow(["Name", "Science", "History", "English", "Total"])
#             csv_writer.writerow([name, science, history, english, total])

#         cont = input("Do you want to add another record? (Y/N): ").lower()
#         if cont != "y":
#             break

# elif UI == "2":
#     # Search for a student's record
#     search = input("Enter the name of the student you want to search: ")
#     found = False

#     with open(file_path, mode="r") as file:
#         csv_reader = csv.reader(file)
#         for row in csv_reader:
#             if row and row[0].lower() == search.lower():  # Case-insensitive match
#                 print(f"Record Found: {row}")
#                 found = True
#                 break

#     if not found:
#         print(f"No record found for student: {search}")

# else:
#     print("Invalid input. Please press '1' or '2'.")
