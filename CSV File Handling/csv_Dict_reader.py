import csv
file_path = "data.csv"

with open(file_path,mode = "r")as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row["Name"], row[" age"], row[" city"])