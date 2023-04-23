import sqlite3

def get_al_data():
    try:
        # Connect to db
        db = sqlite3.connect("app.db")
        print(" Database Connected")

        # Setting up the cursor
        cr = db.cursor()
        
        # Fetch data from db
        cr.execute("SELECT * From users")

        # Assign Data To Variable
        users = cr.fetchall()

        print(f"Number the member is {len(users)}")

        for user in users:
            print(f"id {user[0]}, usename {user[1]}")
    except sqlite3.Error as er:
        print(f"Error {er}")
    finally:
        if db:
            db.close()
            print("Database Closed")

get_al_data()