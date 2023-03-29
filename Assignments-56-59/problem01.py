def calculate(n1,n2,op="add"):
    if(type(int(n1)) != int):
        return "Errore the variable 1 is not number"
    elif(type(int(n2)) != int):
        return "Errore the variable 2 is not number"
    if(op.lower() =="add" or op.lower() == "a"):
        return n1 + n2 
    if(op.lower() =="subtract" or op.lower() == "s"):
        return n1 - n2 
    if(op.lower() =="multiply" or op.lower() == "m"):
        return n1 * n2 
    else:
        return 'Operation Is Not correct'
# Tests
print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200