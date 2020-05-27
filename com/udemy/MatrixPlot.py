import matplotlib.pyplot as plt;
import seaborn as sns;

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

print(tips.head())
print(flights.head())

tcDataset = tips.corr()
print(tcDataset)

# To  show the heatmap
# sns.heatmap(tcDataset,annot= True)

# pivot table
flights_pivot = flights.pivot_table(index='month', columns='year', values='passengers')
print(flights_pivot)

sns.clustermap(flights_pivot)

plt.show()
