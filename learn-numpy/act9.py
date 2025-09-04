import numpy as np

# File data

filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)

# Boolean masking & Advanced indexing

print(filedata > 15)

# Indexing with comparison operators
print(filedata[filedata > 15])

# Indexing with a list
print(filedata[[0],[0,1,2,3,4,5]]) # first 5 elements from 1st row

# masking OR along axis
print(np.any(filedata > 25, axis=0)) # just one element in a col must be above 25 to be true

# masking AND along axis
print(np.all(filedata > 25, axis=0)) # all elememts in a col must be above 25 to be true