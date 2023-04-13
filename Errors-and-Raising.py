x = -10

if(x<0):
    raise Exception(f"The Number {x}")
else:
    print("Good")
print("After If")


x = -10

if(x<0):
    raise ValueError(f"The Number {x}")
else:
    print("Good")
print("After If")