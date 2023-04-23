import sqlite3

db = sqlite3.connect('elzero.db')


# Setting Up The Cursor
cr = db.cursor()

# Create Table users 
cr.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING UNIQUE, dateborthday DATETIME UNIQUE, email STRING UNIQUE)')

# Add data into database
try:
    cr.execute('INSERT INTO users (name, dateborthday, email) VALUES("Sami","20/10/2020","sami@elzero.org")')
    db.commit()
    print("Successfully Insert!")
except sqlite3.Error as sqler: 
    print(f"{sqler} : Error INSERT")

cr.execute('SELECT  * FROM users ORDER BY ID DESC LIMIT 1')

print(cr.fetchone())

id = input('Enter ID : ')

cr.execute(f'SELECT id FROM users WHERE id = {id}')
id_found = cr.fetchone()

print(id_found[0])
print(type(id_found[0]))
print(type(int(id)))
print(id_found == id)

if( id_found == int(id)):
    cr.execute(f'DELETE FROM users WHERE id = {id}')
    db.commit()
    print("User Deleted.")
    cr.execute('SELECT * FROM users')
    users= cr.fetchall()
    print('Show Other Data : ')
    for user in users:
        print(f"ID => {user[0]}, Name => {user[1]}, Date Of Birth => {user[2]}, Email => {user[3]}")
else:
    print("User Not Found.")
db.close()