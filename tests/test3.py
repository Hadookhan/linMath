import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [3,4,5],
    [6,3,4],
    [1,2,2]
])

print(f'Eigenvalues: {np.linalg.eig(A)}\n') # eigenvalues/vectors of A

print(f'Determinant: {np.linalg.det(A)}\n') # determinant of A

print(f'Inverse: {np.linalg.inv(A)}\n') # inverse of A

B = np.array([
    [3,1],
    [0,2]
])

print(f'SVD: {np.linalg.svd(B)}\n') # SVD of B

C = np.array([
    [1,2,1],
    [0,1,2],
    [1,0,1]
])

b = np.array([1,2,3])

Q, R = np.linalg.qr(C)

y = Q.T @ b

print(f'Q: {Q}\n\n R: {R}\n') # QR of C

print(np.linalg.solve(R, y)) # Solve for x

A2 = np.array([
    [2,1],
    [1,3],
    [0,2],
    [1,1]
])

Q2, R2 = np.linalg.qr(A2)

print(Q2)
print(R2)

print(np.allclose(Q2 @ R2, A2))
print(np.allclose(R2, Q2.T @ A2))

U, E, V = np.linalg.svd(B)

print(f'U: {U}\n\nSigma: {E}\n\nV^T: {V}\n')


A = np.array([
    [3,1],
    [0,2]
])

print(A @ A.T)

plt.plot(B)

plt.show()





