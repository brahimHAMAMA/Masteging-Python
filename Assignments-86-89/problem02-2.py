my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    # Write Your Code Here

    if type(item1) == str and type(item2) == str and type(item3) == str:
        if( item1 not in my_data):
            my_data.append(item1)
        if( item2 not in my_data):
            my_data.append(item2)
        if( item3 not in my_data):
            my_data.append(item3)

print("----------------")

final_string = "".join(my_data).capitalize()
print(final_string)