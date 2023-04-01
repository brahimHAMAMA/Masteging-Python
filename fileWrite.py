import os

file = open(fr"{os.getcwd()}\fun.txt","w")

file.write("Line 01\n" *10)


print("=" * 20)
myFrinds=["ali\n","sami\n","omar\n","khalil\n",]
# myfile = open(fr"{os.getcwd()}\osama.txt","w")

# myfile.writelines(myFrinds)

print("=" * 20)
myfile = open(fr"{os.getcwd()}\osama.txt","a")

myfile.writelines(myFrinds)


file.close()