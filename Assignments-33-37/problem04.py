num_one = 10
num_two = 20

# Needed Output
result = num_one + num_two
print(result)
print(result ** 3)
print((result ** 3) % 26000)
print(((result ** 3) % 26000) /5)
print(type(((result ** 3) % 26000) /5))
print(type(str(((result ** 3) % 26000) /5)))

# 30
# 27000
# 1000
# 200.0
# <class 'str'>