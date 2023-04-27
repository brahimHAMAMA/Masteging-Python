import numpy as np

my_list = [1,2,3,4,5,6]
my_list1 = ['A', 'B', 'C']

my_array = np.array(my_list)

print(my_list)
print(my_array)

print("#" *20)

print(type(my_list))
print(type(my_list1))
print(type(my_array))

print("#" *20)

# print(id(my_list[0]))
# print(id(my_list[1]))
# print(id(my_list[2]))
# print(id(my_list[3]))
# print(id(my_array[0]))
# print(id(my_array[1]))
# print(id(my_array[2]))
# print(id(my_array[3]))

print("#" *20)

my_list_data = [1,2,True,False,'a','c',12.3]
my_array_data1 = np.array([1,2,True,False])
# my_array_data= np.array(my_array_data)

print(my_list_data)
print(my_array_data1)
