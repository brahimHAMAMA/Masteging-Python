def myDecorator(func):

    def nestedFun(num1,num2):
        if num1> 20:
            print("Befor")        
            func(num1,num2)
        print("After")

    return nestedFun

def myDecoratorTwo(func):

    def nestedFun(num1,num2):

        print("Befor Decorator 2")        
        func(num1,num2)
        print("After Decorator 2")

    return nestedFun

@myDecoratorTwo
@myDecorator

def CalcSum(num1,num2):
    print( num1 + num2)


CalcSum(100,30)