
alphabie = "abcdefghijklmnopqrstuvwxyz"
giveAlph = "defgi" 

index = alphabie.index(giveAlph[0])
bool = True
for i in range(0, len(giveAlph)):
    if giveAlph[i] != alphabie[index + i]:
        bool = False
        break

print("Ther Is Not missing letter") if bool else print("Ther Is missing letter")

