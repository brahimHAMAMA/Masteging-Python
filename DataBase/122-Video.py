import sqlite3

# Create DB And Connect

db = sqlite3.connect('app.db')

# Setting Up The Cursor
cr = db.cursor()

# create Table and Fields
cr.execute("CREATE TABLE IF NOT EXISTS users (id INTGER, username TEXT)")
cr.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")

# Inserting Data
# cr.execute("INSERT INTO users(id, username) VALUES(1,'BRAHIM')")
# cr.execute("INSERT INTO users(id, username) VALUES(2,'Amina')")
# cr.execute("INSERT INTO users(id, username) VALUES(3,'Ali')")

# my_list = ["Brahim", "Ali","Amina", "Khalil", "Sami"]

# for key, user in enumerate(my_list):
#     cr.execute(f"INSERT INTO users(id, username) VALUES({key +1}, '{user}')")

# Update Data 
cr.execute("UPDATE users SET username = 'ALIA' WHERE id = 1")

# Delete Data.
cr.execute("DELETE FROM users WHERE id=1")
# Fetch Data 
cr.execute("SELECT id, username FROM users")

print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())

# print(cr.fetchall())

# Save Changes
db.commit()

# Close  DataBase

db.close()