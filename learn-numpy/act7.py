import numpy as np

# Statistics

stats = np.array([
    [1,2,3],
    [4,5,6]
    ])
print(stats)

# finds min value on specified axis
print(np.min(stats, axis=1)) # find min on each row

# finds max value on specified axis
print(np.max(stats, axis=1)) # find max on each row

# find sum of matrix
print(np.sum(stats))