import numpy as np

a = np.array([
    [1,2,3,4,5],
    [5,4,3,2,1]
    ])
print(a)

# Matrix addition
b = a + 2
print(b)

# Matrix multiplication
c = a * 3
print(c)

a2 = np.array([
    [6,7,8,9,10],
    [10,9,8,7,6]
    ])

# Matrix multiply another matrix
a3 = a * a2
print(a3)

# sin/cos of matrix
d = np.sin(a)
print(d)
e = np.cos(a)
print(e)