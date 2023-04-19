class BaseOne:
    def __init__(self) -> None:
        print('Base One')
    def funOne(s):
        print('One')
class BaseTwo:
    def __init__(self) -> None:
        print('Base Two')
    def funTwo(s):
        print('Two')

class Derived(BaseTwo, BaseOne):
    pass


my_var = Derived()


# print(Derived.mro())

my_var.funOne()