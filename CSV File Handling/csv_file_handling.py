import csv

file_path = "data.csv"

with open(file_path, mode= "r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    for row in csv_reader:
        print(row[1])