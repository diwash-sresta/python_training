import sqlite3

def connect_db(db_path):
    conn = sqlite3.connect(db_path)
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY ,
               username TEXT NOT NULL ,
               age INTEGER,
               email TEXT UNIQUE    
               )

               ''')
    conn.commit()

def insert_user(conn, username, age , email):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, age, email) VALUES (?, ?, ?)", (username,age,email))
    conn.commit()
    print("Record inserted successfully!")

def display_users(conn):
     cursor = conn.cursor()
     cursor.execute("SELECT * FROM users")
     rows = cursor.fetchall()
     return rows

def search_user_by_id(conn, user_id):
     cursor = conn.cursor()
     cursor.execute("SELECT * FROM users WHERE id = ? ",(user_id,))
     return cursor.fetchall()

def update_user_age(conn, username, new_age):
     cursor = conn.cursor()
     cursor.execute("UPDATE users SET age = ? WHERE username = ?",(new_age, username))
     if cursor.rowcount > 0:
          conn.commit()
          print(f"Age updated successfully for user : {username}")
     else:
        print(f"No user found with username: {username}")

def delete_user_by_id(conn,user_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?",(user_id,))
    return cursor.fetchall()
