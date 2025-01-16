import csv 
data = [
    ["Alice", 30 , "London"]
    ["Bob", 23, "Paris"]
    ["Charlie", 32 , "Berlin"]
]
file_path ="write.csv"
with open(file_path, mode = "w", newline = "") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Name","Age","City"])
    for row in data:
        csv_writer.writerow(row) 