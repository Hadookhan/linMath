import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# plot x/y graph


x = [0,1,2,3,4]
y = [0,2,4,6,8]
#plt.plot(x,y, label='2x', color='red', marker='.', markersize=10, markeredgecolor='black', linestyle='--')

# Resize resolution size
plt.figure(figsize=(7,4), dpi=200)

# shorthand notation for plotting ([colour][marker][line])
plt.plot(x,y, 'b.--', label='2x')

# configure graph labels
plt.title('First Graph')
plt.xlabel('X axis')
plt.ylabel('Y axis')

# configure x-y increments (resizes graph)
plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8])

# creates array starting from 0, stopping at 4, stepping 0.5
x2 = np.arange(0,4,0.5)
print(x2)
plt.plot(x2,x2**2, 'k.-', label='x2^2')

# displays plotting labels
plt.legend()

# save graph
plt.savefig('saved/mygraph.png', dpi=200)

# displays graph
plt.show()