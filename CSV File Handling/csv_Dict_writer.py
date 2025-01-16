import csv

data = [
    {"Name": "Alice", "Age": 30 , "City":"London"},
    {"Name": "Bob", "Age": 22 , "City":"Paris"},
    {"Name": "Charlie", "Age": 21 , "City":"Berlin"},

]

file_path = "output.csv"
fieldnames = ["Name", "Age", "City"]

with open(file_path,mode = "w",newline="")as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)