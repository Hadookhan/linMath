import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6,4), dpi=100)

N = 100
x = np.linspace(1, 10, N+1) # creates an array with 100 elements between 1-10
y = x**2 + np.sin(x) # equation to be differentiated
dydx = np.gradient(y, x)
y_int = np.cumsum(y) * (x[1]-x[0])

plt.plot(x,y, label='original')
plt.plot(x, dydx, label='derivative')
plt.plot(x, y_int, label='integrate')

A = np.array([
    [1,2,0],
    [0,3,4],
    [0,0,2]
])

print(np.linalg.eig(A))

eigvalsA, eigvecsA = np.linalg.eig(A)

λ = eigvalsA[1]
v = eigvecsA[:,1]

print("Check Av vs λv:")
print(np.dot(A, v))       # A v
print(λ * v)              # λ v

for i in range(len(eigvalsA)):
    λ = eigvalsA[i]
    v = eigvecsA[:, i]
    #plt.plot(np.real(λ * v), label=f'λa={λ:.2f}')

# 2
B = np.array([
    [4,1,0],
    [0,2,3],
    [0,0,5]
])

eigvalsB, eigvecsB = np.linalg.eig(B)

print(eigvalsB)

valB = eigvalsB[1]
vecB = eigvecsB[:,1]

print("Check Bv vs λv:")
print(np.dot(B, vecB))       # A v
print(valB * vecB)           # valB v

for i in range(len(eigvalsB)):
    λ = eigvalsB[i]
    v = eigvecsB[:, i]
    #plt.plot(np.real(λ * v), label=f'λb={λ:.2f}')

plt.legend()

plt.show()