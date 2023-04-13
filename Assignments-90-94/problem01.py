NUM = input("Add Your Number ")

# Your Code Here

if len(NUM) > 1:
  raise IndexError("Only One Character Allowed")
elif(NUM == 0):
  raise ValueError("Number Must Be Larger Than 0")
elif(type(NUM) != int):
  raise Exception("Only Numbers Allowed") 
else:
  print(f"The Number Is {NUM}")
