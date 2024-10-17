import seaborn as sns
import matplotlib.pyplot as plt

from D598_Task2 import ds

# Calculate average profit margin by state
profit_margin_by_state = ds.groupby('Business State')['Profit Margin'].mean().reset_index()

# Pivot the data for a heatmap
heatmap_data = profit_margin_by_state.pivot_table(index='Business State', values='Profit Margin')

# Plot: Heatmap of Average Profit Margin by State
plt.figure(figsize=(10,6))
sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title('Average Profit Margin by State')
plt.ylabel('State')
plt.xlabel('Average Profit Margin')
plt.show()
