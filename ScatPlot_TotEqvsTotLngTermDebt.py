# Plot: Total Equity vs. Total Long-term Debt
from matplotlib import pyplot as plt

from D598_Task2 import ds

plt.figure(figsize=(10,6))
plt.scatter(ds['Total Equity'], ds['Total Long-term Debt'], color='purple')
plt.xlabel('Total Equity')
plt.ylabel('Total Long-term Debt')
plt.title('Total Equity vs. Total Long-term Debt')
plt.show()
