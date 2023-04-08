my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []

for data in zip(my_list, my_tuple):
  # Write Your Code Here
  my_data.append(data[0])
  my_data.append(data[1])




final_string = "".join(my_data).capitalize()
print(final_string) # Elzero