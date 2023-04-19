from multinherit.multinherit import multi_super

class A:
    def __init__(self, one):
        self.one = one

class B:
    def __init__(self, two):
        self.two = two

class C:
    def __init__(self, three):
        self.three = three

# Write The Class Called "Text" Here
class Text(A, B, C):
    def __init__(self, one, two, three):
        multi_super(A, self, one=one)
        multi_super(B, self, two=two)
        multi_super(C, self, three=three)

    def show_name(self):
        name = self.one + self.two + self.three
        return f"The Name Is {name}"

the_name = Text("El", "ze", "ro")

print(the_name.show_name())

# Ouput
# The Name Is Elzero