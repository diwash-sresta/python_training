import traceback
def divide():
    print("hello before try except")
    try:
        x = int(input("enter the number of x"))
        y = int(input("enter the number of y"))
        result = x/y
        print("result",result)
    except Exception as e:
        traceback.print_exc()
        print(f"handle all exception{e}")

divide()