class Member:
    def __init__(self, name) -> None:
        self.__name = name

    def say_hello(self):
        return f"Hello {self.__name}"
    
    def get1_name(self):
        return self.__name
    
    def set1_name(self, new_name):
        self.__name = new_name
member1 =Member('ali')

print(member1.say_hello())
print(member1.get1_name())
member1.set1_name("brahim")
print(member1.get1_name())
