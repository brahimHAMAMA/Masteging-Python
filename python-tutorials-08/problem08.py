num = 8
list = []
for i in range(1, num + 1):
    list.append(i)

print(list)
print("".join(map(str, list)))

print("="*20)

for i in range(1, num + 1):
    print(i, end="") 
