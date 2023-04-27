# ---------------------------------------------
# -- Numpy => Arithmetic & Useful Operations --
# ---------------------------------------------
# - Addition
# - Subtraction
# - Multiplication
# - Dividation
# ----------------
# - min
# - max
# - sum
# - ravel => Returns Flattened Array 1 Dimension With Same Type
# ----------------------------------------------

import numpy as np

# Arithmetic Operations

my_array1 = np.array([10, 20, 30])
my_array2 = np.array([5, 2, 4])

# print(my_array1 + my_array2)
# print(my_array1 - my_array2)
# print(my_array1 * my_array2)
# print(my_array1 / my_array2)

my_array3 = np.array([[1, 4], [5, 9]])
my_array4 = np.array([[2, 7], [10, 5]])

print(my_array3 + my_array4)
print(my_array3 - my_array4)
print(my_array3 * my_array4)
print(my_array3 / my_array4)


print(my_array1.min())
print(my_array1.max())
print(my_array1.sum())

print(my_array4.ravel())