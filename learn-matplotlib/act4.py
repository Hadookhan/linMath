import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fifa = pd.read_csv('data/fifa_data.csv')

bins = [40,50,60,70,80,90,100]

# histogram (bins = x-axis reaccurances)
plt.hist(fifa.Overall, bins=bins)

plt.xticks(bins)

plt.ylabel('No. of Players')
plt.xlabel('Skill Rating')
plt.title('Distribution of Player Rating (FIFA 18)')

plt.show()

# pandas loc method is used to look up items in datasets
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]

labels = ['Left','Right']

plt.pie([left, right], labels=labels, colors=['grey','white'], wedgeprops={"linewidth": 1, "edgecolor": "black"}, autopct='%.2f%%')

plt.title('Foot preferrence of FIFA players')

plt.show()