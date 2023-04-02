import os
print(f"{os.path.basename(__file__)}")
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))

newDir = "newDirectory1"
parentDir = os.path.dirname(__file__)

path = os.path.join(parentDir, newDir)
if os.path.exists(path):
    
    print("The Directory is existing")
else:
    os.mkdir(path)
    print("Directory Created")
print(path)