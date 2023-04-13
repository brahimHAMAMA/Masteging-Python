LETTER = input("Add Letter From A to Z ")

# Your Code Here

try :
    len(LETTER) == 1
    print(len(LETTER))
except TypeError:
    print("You Must Write One Character Only")
else:
    print(f"You Typed {LETTER}")