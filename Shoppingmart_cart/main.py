items = {
    "1.Kurkuree 85gm": 50,
    "2.Shampoo 200ml": 300,
    "3.Mixed packed Vegetable 1kg": 750,
    "4.Coca-Cola 2.5L": 260,
    "5.Face_wash 200gm": 270,
    "6.Sunscream 200gm": 850,
}

items_cart = {}
while True:
    UI = '''
                Welcome to Super Shopping Mart!!!!

                1. Enter the mart
                2. Exit the mart
    '''
    print(UI)

    try:
        options = int(input("Enter (1-2) to continue: "))
    
        if options == 2:
            print("\nYour Cart Summary:")
            if items_cart:
                total = 0
                for item, qty in items_cart.items():
                    price = items[item]  
                    total += price * qty
                    print(f"{item} - Nrs.{price} x {qty} = Nrs.{price * qty}")
                print(f"\nTotal: Nrs.{total}")
            else:
                print("Your cart is empty.")
            print("\nThank you for visiting Super Shopping Mart!")
            break

        elif options == 1:
            print("\nWelcome to the mart! Here are the available items:\n")
            for item, price in items.items():
                print(f"{item} - Nrs.{price}")
            
            while True:
                item_choice = input("\nEnter the item number to add to cart (or type 'done' to stop): ").strip()
                
                if item_choice.lower() == "done":
                    break
                
                # Match item number to the dictionary key
                matching_key = next((key for key in items.keys() if key.startswith(f"{item_choice}.")), None)
                
                if matching_key:
                    try:
                        quantity = int(input(f"Enter quantity for {matching_key}: "))
                        if quantity <= 0:
                            print("Quantity must be greater than zero. Please try again.")
                            continue
                        if matching_key in items_cart:
                            items_cart[matching_key] += quantity
                        else:
                            items_cart[matching_key] = quantity
                        print(f"\n{quantity} x {matching_key} added to your cart.")
                    except ValueError:
                        print("Invalid quantity. Please enter a valid number.")
                else:
                    print("Invalid item number. Please select a valid item.")

            print("\nCurrent items in cart:")
            for item, qty in items_cart.items():
                print(f"{item} - Quantity: {qty}")
                
        else:
            print("Invalid input. Please input a valid number (1 or 2).")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
