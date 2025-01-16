import sqlite3

conn = sqlite3.connect("E:\python traiing\Database\data.db")
print(conn)

cursor = conn.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#                id INTEGER PRIMARY KEY ,
#                username TEXT NOT NULL ,
#                age INTEGER,
#                email TEXT UNIQUE    
#                )

#                ''')

# Inseet a single record
username = input("Enter the username")
cursor.execute("INSERT INTO users (username, age, email) VALUES (?, 30, 'alice@example.com')", (username,))
conn.commit()

# Insert multiple records

# users = [
#     ('Bob', 25 , 'bob@example.com'),
#     ('Charlie',35,'charlie@example.com')
# ]
# cursor.executemany("INSERT INTO users (username, age, email) VALUES (?, ?, ? ),users")
conn.commit()