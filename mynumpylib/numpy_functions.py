import numpy as np

# arange illustration
a_range_arr = np.arange(10) # start from 0 and ends at 9
np_range_arr = np.arange(10, 21) # start from 10 and ends at 20
np_range_jump_arr = np.arange(10, 21, 3) # start from 10 and jump 3 steps
print(a_range_arr)
print(np_range_arr)
print(np_range_jump_arr)

# random illustration
a = np.random.permutation(np.arange(10))
print(a)
# create multidimensional array using random
# It creates a three-dimensional array which contains
#  -  2 two-dimensional array
#  -  Each two-dimensional array contains 3 one-dimensional array
#  -  Each one-dimensional array contains 2 elements

rand_mul_dim = np.random.rand(2, 3, 2)
print(rand_mul_dim)

# reshape illustration
reshaped_arr = np.arange(100).reshape(4, 25)
print(reshaped_arr.shape)
print(reshaped_arr)