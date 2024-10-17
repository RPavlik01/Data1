import matplotlib.pyplot as plt

from D598_Task2 import ds

# Plot: Debt-to-Income Ratio by State
plt.figure(figsize=(10,6))
plt.bar(ds['Business State'], ds['Debt-to-Income Ratio'], color='blue')
plt.xlabel('State')
plt.ylabel('Debt-to-Income Ratio')
plt.title('Debt-to-Income Ratio by State')
plt.xticks(rotation=45)
plt.show()
