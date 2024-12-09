# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# for i in range(10):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
#                    (f"User{i+1}",f"example{i+1}@gmail.com", str((i+1)*10), "1000"))
#

# for i in range(5):
#     #print(2*i + 1)
#     cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", ("500",f"User{((2*i)+1)}"))

for i in range(4):
    print(3*i+1)
    #cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{(3*i)+1}"),)
    cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{((3*i)+1)}",))

connection.commit()
connection.close()