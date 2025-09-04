import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv('data/gas_prices.csv')

plt.figure(figsize=(8,5))

plt.title('Gas Prices over Time (USD)')

# plt.plot(gas.Year, gas.USA, 'b.-', label='USA')
# plt.plot(gas.Year, gas.Canada, 'r.-', label='Canada')
# plt.plot(gas.Year, gas['South Korea'], 'g.-', label='South Korea')

for country in gas:
    if country != 'Year':
        plt.plot(gas.Year, gas[country], '.-', label=f'{country}')

plt.xticks(gas.Year[::2])

plt.xlabel('Year')
plt.ylabel('USD ($)')

plt.legend(title='Countries')

plt.savefig('saved/gasPrices.png', dpi=200)
plt.show()