import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# plot bar chart


labels = ['A','B','C']
values = [1,4,2]

plt.figure(figsize=(6,4), dpi=200)
bars = plt.bar(labels,values, label='bars')

# customise look of bars
bars[0].set_hatch('/')

plt.title('Bar Chart')
plt.yticks([0,1,2,3,4])
plt.ylabel('y')

plt.legend()

plt.show()