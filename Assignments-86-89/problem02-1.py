my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    # Write Your Code Here
    my_data.append(item1)
    my_data.append(item2)
    my_data.append(item3)

print("----------------")

StringItem = lambda item : type(item) == str

my_dataFilter = filter(StringItem, my_data)
my_dataFilter = list(my_dataFilter)



final_string = "".join(my_dataFilter).capitalize()
print(final_string)