import numpy as np

a = np.ones((5,5))

b = np.zeros((3,3))
b[1,1] = 9

a[1:-1,1:-1] = b

print(a)

# careful when copying arrays:
c = a.copy()