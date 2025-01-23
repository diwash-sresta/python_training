import csv

file_path = "E:\python_training\CSV File Handling\data1.csv"

with open(file_path, mode= "r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    for row in csv_reader:
        print(row[1])