
# Input
name = "OSAMA"

# Needed Output
my_friends =[]
nax_num =4
i= 0
while i < nax_num:
    theName = input("Inter tne name : ").strip()
    if (theName.isupper()):
        print("Invalid Name")
    elif (theName[0].isupper()):
        my_friends.append(theName) 
        print(f"Friend {theName} Added")
        print(f"Names Left in List Is {nax_num - (i +1)}")
        i = i + 1
    else:
        my_friends.append(theName.capitalize()) 
        print(f"Friend {theName} Added => {i +1} er Letter Become Capital") if (i+1 ==1) else print(f"Friend {theName} Added => {i +1} eme Letter Become Capital")
        print(f"Names Left in List Is {nax_num - (i +1)}")
        i = i + 1
print(my_friends)
"Invalid Name"

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")