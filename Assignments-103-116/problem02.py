class User:
  # Write Class Content
    def __init__(self, fname, lname, age, gender) -> None:
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

    def full_details(self):
        age_calc = "0" + str(40 - self.age) if (40 - self.age) < 10 else (40 - self.age)

        return f"Hello Mr {self.fname} {self.lname[0].upper()}. [{age_calc}] Years To Reach 40" if(self.gender == 'Male')\
                else f"Hello Mss {self.fname} {self.lname[0].upper()}. [{age_calc}] Years To Reach 40" 
user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40