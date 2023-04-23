# -----------------------------------------------------
# -- Databases => SQLite => Create Skills App Part 2 --
# -----------------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("Practice.db")

# Setting Up The Cursor
cr = db.cursor()

# Commit and Close Method
def commit_and_close():
    # Save (Commit) Changes
    db.commit()
# Close Database
    db.close()

# My User ID
uid = 2

# Input Big Message
input_message = """
What Do You Want To Do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option : """

# Input Option Choose

user_input = input(input_message).strip().lower()

# Command List
commands_list = ["s", "a", "d", "u", "q"]

# Define The Methods
def show_skills():
    skill_id = input('Enter ID skill : ')
    try:
        cr.execute(f"SELECT * FROM skills WHERE id = {skill_id}")
        return cr.fetchone()
    except sqlite3.Error as er:
        print(f" {er} : ID {skill_id} Not Exist")

def add_skill():
    cr.execute("CREATE TABLE IF NOT EXISTS skills(id INTEGER PRIMARY KEY AUTOINCREMENT, skill STRING, progress STRING, user_id INTEGER)") # PRIMARY KEY AUTOINCREMENT
    skill = input('Enter skill : ')
    progress = input("Enter progress : " )
    user_id = input("Enter User ID : " )

    cr.execute(f"INSERT INTO skills(skill, progress, user_id) VALUES('{skill}','{progress}', '{user_id}')")
    print(f'The skill {skill} has added')
    commit_and_close()

def update_skill():
    skill_old = show_skills()
    print(skill_old)
    skill = input('Enter skill : ')
    progress = input("Enter progress : ")
    cr.execute(f"update skills set skill = {skill} where id = '4'")

    print(f"Skill ID {skill_old[0]} has Updated!")

    # try:

    #     cr.execute(f"UPDATE skills SET skill = {skill} WHERE id = {skill_old[0]}")
    #     print(f"Skill ID {skill_old[0]} has Updated!")
    # except sqlite3.Error as er:
    #     print(f" {er} : ID {skill_old[0]} Not Exist")
    # finally:
    #     commit_and_close()
def delete_skill():
    skill_id = input('Enter ID skill : ')
    show_skills()
    try:
        cr.execute(f"DELETE FROM skills WHERE id = {skill_id}")
        print(f"Skill ID {skill_id} has Deleted!")
    except sqlite3.Error as er:
        print(f" {er} : ID {skill_id} Not Exist")
    finally:
        commit_and_close()
# Check If Command Is Exists

while user_input  not in commands_list:

    print(f"Sorry This Command \"{user_input}\" Is Not Found")
    # Input Option Choose
    user_input = input(input_message).strip().lower()

else:

    # print(f"Command Found {user_input}")

    if user_input == "s":   
        print (show_skills()) 
        commit_and_close()

    elif user_input == "a": 
        add_skill()   
    elif user_input == "d": 
        delete_skill()    
    elif user_input == "u": 
        update_skill()    
    else:
        commit_and_close()
        print("App Is Closed.")