# Plot: Histogram of Total Revenue
from matplotlib import pyplot as plt

from D598_Task2 import ds

plt.figure(figsize=(10,6))
plt.hist(ds['Total Revenue'], bins=20, color='green', edgecolor='black')
plt.xlabel('Total Revenue')
plt.ylabel('Frequency')
plt.title('Distribution of Total Revenue')
plt.show()
