import matplotlib.pyplot as plt
import seaborn as sns;

tips = sns.load_dataset('tips')
print(tips.head())

# sns.barplot(x='sex',y='total_bill',data=tips)
# sns.boxplot(x = 'sex',y = 'total_bill',data=tips)

# vilionplot
sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)

plt.show()
