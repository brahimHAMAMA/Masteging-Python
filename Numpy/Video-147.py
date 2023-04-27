# -------------------------------------------
# -- Numpy => Data Types And Control Array --
# -------------------------------------------
# https://numpy.org/devdocs/user/basics.types.html
# https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#specifying-and-constructing-data-types
# -------------------------------------------
# '?' boolean
# 'b' (signed) byte
# 'B' unsigned byte
# 'i' (signed) integer
# 'u' unsigned integer
# 'f' floating-point
# 'c' complex-floating point
# 'm' timedelta
# 'M' datetime
# 'O' (Python) objects
# 'S', 'a' zero-terminated bytes (not recommended)
# 'U' Unicode string
# 'V' raw data (void)
# ------------------------------------------------

import numpy as np

# Show Array Data Type

my_array1 = np.array([1, 2, 3])
my_array2 = np.array([1.5, 20.15, 3.601])
my_array3 = np.array(["Osama_Elzero", "B", "Ahmed"])


print(type(my_array1))
print(type(my_array2))
print(type(my_array3))

print(my_array1.dtype)
print(my_array2.dtype)
print(my_array3.dtype)


print('#' * 20)

#Create Array and Specific data type

my_array4 = np.array([1, 2, 3], dtype=float)
my_array5 = np.array([1.5, 20.15, 3.601], dtype=int)
my_array6 = np.array(["Osama_Elzero", "B", "Ahmed"], dtype=str)


print(my_array4.dtype)
print(my_array5.dtype)
print(my_array6.dtype)

print('#' * 20)

# change data type of Existing Array
my_array7 = np.array([1, 2, 3,5,6,7])
print(my_array7.dtype)
print(my_array7)

my_array7 = my_array7.astype(float)

print(my_array7.dtype)
print(my_array7)


my_array7 = my_array7.astype(bool)

print(my_array7.dtype)
print(my_array7)

print('#' * 20)
#Test Capacity
my_array8 = np.array([100, 200, 300, 500, 600, 700], dtype='f')
print(my_array8.dtype)
print(my_array8[0].itemsize)
