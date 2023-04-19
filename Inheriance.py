class Food:
    def __init__(self, name):
        self.name = name
        print("Food Is Created From Main Class")

    def eat(self):
        print("Eat Method From Base Class")

class Appel(Food):
    def __init__(self, name) -> None:
        super().__init__(name)
        print(f"{self.name} is created from Derived class")

food1 = Food("Pizza")
food2 = Appel("Pizza")

food2.eat()
# food2.eat()