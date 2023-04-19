class Member:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


    def say_hello(self):
        return f"Hello {self.name}"
    
    @property
    def age_in_age(self):
        return self.age *365

member1 =Member('ali', 40)


print(member1.name)
print(member1.age)
print(member1.say_hello())
# print(member1.age_in_age())
print(member1.age_in_age)
