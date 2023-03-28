# Input
for i in range(1,20):
    if(i ==6 or i == 8 or i == 12):
        continue
    print(f"0{i}") if i<10 else print(i)
else:
    print("All Numbers Printed")