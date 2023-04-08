def myDecorator(func):

    def nestedFun():
        print("Befor")        
        func()
        print("After")

    return nestedFun

@myDecorator
def sayHello():
    print("Hello From Say Hello Function")
@myDecorator
def sayHowAreYou():
    print("How Are You From HowAreYou Function")

sayHello()


print("="*30)
sayHowAreYou()
# aftenDec = myDecorator(sayHello)
# aftenDec()