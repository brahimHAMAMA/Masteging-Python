from time import time

def SpeedTime(fun):
    def nestedFun():
        startT = time()
        fun()
        endT = time()
        print(f"Time for loop Is : {endT - startT}")
    return nestedFun


@SpeedTime
def begLoop():
    for i in range(1,300):
        print(i)

begLoop()