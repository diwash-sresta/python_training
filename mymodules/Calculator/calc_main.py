from calc_functions import add, sub , mul , div , expo, f_div, mod


while True:
    UI = '''
    display options  :

    1.add                   4.division          7.modulus
    2.substraction          5.exponential       
    3.multiplication        6.floor division    8.exit
    '''
    print (UI)

    operation = int(input("Select the  opertaion you want to perfrom :"))
    
    if operation == 8:
        print("Exiting the program")
        break

    n1 = int(input("Enter the first number :"))
    n2 = int(input("Enter the second number :"))


    if operation == 1:
        result = add(n1,n2)
        print(f"Result : {result}")

    elif operation == 2:
        result = sub(n1,n2)
        print(f"Result : {result}")
    
    elif operation == 3:
        result = mul(n1,n2)
        print(f"Result : {result}")

    elif operation == 4:
        result = div(n1,n2)
        print(f"Result : {result}")

    elif operation == 5:
        result = expo(n1,n2)
        print(f"Result : {result}")

    elif operation == 6:
        result = f_div(n1,n2)
        print(f"Result : {result}")

    elif operation == 7:
        result = mod(n1,n2)
        print(f"Result : {result}")