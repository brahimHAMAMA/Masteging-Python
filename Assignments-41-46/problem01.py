# Inputs

num1 = input("Inter num 1 : ").strip()
num2 = input("Inter num 2 : ").strip()
operation = input("Inter Operator : ").strip()
num1 = int(num1)
num2 = int(num2)
print(type(num1))
print(type(num2))
if (operation == "+"): print(f"{num1} + {num2} = {num1 + num2}")
elif (operation == "-"): print(f"{num1} - {num2} = {num1 - num2}")
elif (operation == "*"): print(f"{num1} * {num2} = {num1 * num2}")
elif (operation == "/"): print(f"{num1} / {num2} = {num1 / num2}")
elif (operation == "%"): print(f"{num1} % {num2} = {num1 % num2}")
else: print("there is note operation...")

# operation = "+" Or "-" Or "*" Or "/" Or "%"

# Needed Output

# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800