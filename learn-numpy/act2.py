import numpy as np

a = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
    ])

# Item shape (2, 5)
# print(a.shape)

# Specify index [i][j]
print(a[0, 1]) # 2

# Specify row
print(a[0, :])

# Specify col
print(a[:, 0])

# index syntax
print(a[0, 1:4:2]) # startIndex:stopIndex:stepIndex

# modify value
a[-1, -1] = 100
print(a)