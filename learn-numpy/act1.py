import numpy as np

a = np.array([1,2,3], dtype='int32')
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b)

# get dimension
print(a.ndim)

# get shape
print(a.shape)

# get type
print(a.dtype)

# get item size
print(a.itemsize)

# get size
print(a.size)

# get total size
print(a.nbytes)
