my_set = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output
print(my_set)
my_set.clear()
print(my_set)
my_set.add("A")
my_set.add("B")
print(my_set)
my_set.discard("C")
# {1, 2, 3}
# set()
# {"A", "B"}