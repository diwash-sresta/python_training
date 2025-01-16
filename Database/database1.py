from database1_functions import connect_db,create_table, insert_user, display_users, search_user_by_id, update_user_age,delete_user_by_id

db_path =r"E:\python_training\Database\data2.db"

conn =connect_db(db_path)

create_table(conn)

UI = '''
Display options :
1.Display all records
2.Insert data
3.Search data by ID
4.Update data by username
5.Delete data by id
6.Exit
'''
print(UI)

while True:
    try:
        options = int(input('''Enter your choice (1 - 5):'''))

        if options == 1 :
            users = display_users(conn)
            print("Users Table:")
            for user in users:
                print(user)

        elif options == 2: 
            username = input("Enter the username : ")
            age = int(input("Enter age : "))
            email = input("Enter email : ")
            insert_user(conn, username, age, email)



        elif options == 3:
            user_id = int(input("Enter the user ID to search : "))
            user = search_user_by_id(conn, user_id)
            if user :
                print(f"Record Found: {user}")
            else:
                print(f"No record found with the given ID.")

        elif options ==4:
            username = input("Enter the username to update: ")
            new_age = int(input(f"Enter the new age for {username}: "))
            update_user_age(conn, username, new_age)

        elif options == 5:
            user = delete_user_by_id(conn, user_id)
            if user :
                print(f"Record deleted: {user}")
            else:
                print(f"No record found with the given ID.")
        
        elif options == 6:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1 and 5.")
    except ValueError:
        print("Invalid input! Please enter a numeric value for your choice.")
    except Exception as e:
        print(f"An error occured: {e}\n")

conn.close()
