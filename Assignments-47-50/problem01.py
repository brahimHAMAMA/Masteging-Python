num = int(input("Inter number please : ").strip())

while num<=0:
    print("the number inter it is 0 or less, ")
    num = int(input("please inter number agune : ").strip())
for i in range(num, 0,-1):
    if i != 6:
        print(i)