import numpy as np

np_list = np.array([1, 2, 3, 5, 7], dtype='i')
np_tuple = np.array((1, 2, 3, 5, 7), dtype='f')

# We can explicitly define the type of elements of a numpy array
np_typed_tuple = np.array((1, 2, 3, 5, 7), dtype='f')
print(np_list)
print(np_tuple)
print(type(np_list)) # class numpy.ndarray
print(type(np_typed_tuple)) # class numpy.ndarray
print(np_typed_tuple.dtype) # float32

# Multidimensional numpy array
# If we want to define multidimensional arrays then at each dimension
# we should have equal numbers of elements
np_muldim_list = np.array([[5, 6, 10, 11], [2, 8, 15, 25]])
print(np_muldim_list[0][0])
print(np_muldim_list[0, 3]) # Accessing numpy array elements
print(np_muldim_list.ndim) # Get the dimension of the array.
print("shape np_muldim_list = ", np_muldim_list.shape)
# define 3 dimension array
np_three_dim_array = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[10, 12, 13, 14], [25, 26, 27, 28], [30, 31, 32, 33]]])
print(np_three_dim_array.ndim)
print(np_three_dim_array[1, 1, 2])
print("shape np_three_dim_array = ", np_three_dim_array.shape)

# print(np_muldim_list.shape[0], np_muldim_list.shape[1]) # Get the dimension of the array.