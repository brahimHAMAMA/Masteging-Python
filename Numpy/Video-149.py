# ------------------------------------
# -- Numpy => Array Shape & ReShape --
# ------------------------------------
# Shape Returns A Tuple Contains The Number Of Elements in Each Dimension
# ----------------------------------------------

import numpy as np

# my_array1 = np.array([1, 2, 3, 4])
# print(my_array1.ndim)
# print(my_array1.shape)


# print("#" * 50)
# my_array2 = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
# print(my_array2.ndim)
# print(my_array2.shape)



my_array4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(my_array4.ndim)
print(my_array4.shape)

reshaped_array4 = my_array4.reshape(3,4)
print(reshaped_array4)
print(reshaped_array4.ndim)
print(reshaped_array4.shape)
