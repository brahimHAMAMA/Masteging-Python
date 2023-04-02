
Substring= "o"
String= "I Love Elzero Web School"


count= 0
for i in range(0, len(String)):
    if String[i] == "o":
        count = count + 1
print(count)

print("="*20)
count1= 0
for i in range(0, len(String)):
    if "o" in String[i] :
        count1 += 1
print(count1)



print("="*20)
count1= 0
for letter in String:
    if "o" == letter :
        count1 += 1
print(count1)
