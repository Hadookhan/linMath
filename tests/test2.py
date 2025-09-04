import numpy as np
import matplotlib.pyplot as plt

## y = e^-x/10 * sin(x)

N = 10000
x = np.linspace(-5,5,N+1)
y = -5*(x)**2 - 30*x - 40
dydx = np.gradient(y,x)
#y_int = np.cumsum(y) * (x[1]-x[0])


plt.plot(x,y, label='xy')
plt.plot(x, dydx, label='dydx')
#plt.plot(x, y_int, label='y_int')

plt.legend()
plt.show()