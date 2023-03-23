nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output
# nums.union(letters)
print(nums | letters)
print(nums.union(letters))
nums.update(letters)
print(nums)

# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}