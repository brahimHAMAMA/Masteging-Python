# Input
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
i=0
num_ignore= 0
while i< len(friends):

    if (friends[i].islower()):
        num_ignore = num_ignore + 1
    else:
        print(friends[i])
    i = i +1

print(f"Friends Printed And Ignored Names Count Is {num_ignore}")
# Needed Output
"Mohamed"
"Shady"
"Sherif"
"Friends Printed And Ignored Names Count Is 2"