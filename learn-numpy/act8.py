import numpy as np

# Reorganizing arrays

before = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
    ])
print(before)

# resize must match shape of original matrix
after = before.reshape((5,2))
print(after)

# vertically stacking vectors

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack((v1,v2)))

# horizontally stacking vectors

h1 = np.zeros((3,5))
h2 = np.ones((3,2))

print(np.hstack((h1,h2)))