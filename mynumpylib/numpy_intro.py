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