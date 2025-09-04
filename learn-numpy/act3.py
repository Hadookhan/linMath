import numpy as np
from act2 import a

# initialize 0s matrix
print(np.zeros((3,10))) # arg1=shape tuple (r, c)

# init 1s matrix
print(np.ones((3,3,10))) # 3d shape (z, x, y)

# init empty/custom matrix
print(np.full((2,2), 99)) # fill 2x2 matrix with 99

# init inherited matrix shape
print(np.full_like(a, 4))

# init random decimal values into new matrix shape
print(np.random.rand(4,2))

# init random decimal values into inherited matrix shape
print(np.random.random_sample(a.shape))

# init random integer values with given min/max int into new matrix shape
print(np.random.randint(2, 7, size=(3,3))) # max value is exclusive

# init identity matrix
print(np.identity(5)) # one param because I=Square matrix

# repeat array
r1 = np.repeat(a,3, axis=0)
print(r1)