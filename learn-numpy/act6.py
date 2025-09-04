import numpy as np
from numpy.linalg import det, inv, eig, eigvals, solve

# Linear algebra

a = np.ones((2,3))
print(a)

b = np.full((3,2), 2)
print(b)

# find the determinant
c = np.identity(3)
print(det(c))

# find matrix dot product
# option 1
d = np.dot(a, b)
print(d)
# option 2
print(a @ b)
# option 3 (implements option 2)
z = np.matmul(a,b)
print(z)

v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

# find vector dot product
e = np.vdot(v1, v2)
print(e)

# find inner product of vectors (scalar output)
inner = np.inner(v1,v2)
print(inner)

# find outer product of vectors (matrix output)
outer = np.outer(v1,v2)
print(outer)

# Matrix to be inversed -> CANNOT be singular matrix (determinant != 0)
m = np.array([ 
    [1, 2],
    [3, 4]
    ])

# inverse matrix
print(inv(m))

m = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
])

# finds eigenvalues/eigenvectors of matrix
print(eig(m))
print(eigvals(m))

# tracing matrix (sum of eigenvalues)
print(np.trace(m))

# product of eigenvalues = determinant
print(det(m))

A = np.array([
    [2,-1,3],
    [4,2,1],
    [-2,1,2]
])

B = np.array([
    [5],
    [12],
    [-1]
])

# solves for x vector using linear matrix
x = solve(A,B)
print(x)

C = np.array([
    [1,2,0],
    [0,3,4],
    [0,0,2]
])

print(eig(C))
print(eig(C)[1][1])

eigval, eigvecs = np.linalg.eig(C)

λ = eigval[1]
v = eigvecs[:,1]

print("Check Av vs λv:")
print(np.dot(C, v))       # A v
print(λ * v)              # λ v
