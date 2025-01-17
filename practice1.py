n = int(input("Enter the number of rows: "))
for i in range(n+1):  # Loop through rows
    for j in range(n+1 - i):  # Loop through columns in each row
        print(j+1, end="")  # Print numbers in each row
    print()
