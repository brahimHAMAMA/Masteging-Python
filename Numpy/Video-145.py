import numpy as np
import time
import sys

elements = 1500
my_list1 = range(elements)
my_list2 = range(elements)

my_array1 = np.arange(elements)
my_array2 = np.arange(elements)

time_start = time.time()
# list_result = [(n1 + n2) for n1, n2 in zip(my_list1, my_list2)]
list_result = my_array1 + my_array2
# for n1, n2 in zip(my_list1, my_list2):
#     print(n1 + n2)

for n in list_result:
    print(n)
# print(list_result)
time_end = time.time()
time_total = time_end - time_start


print(time_total)
# for n in my_array1:
#     print(n)