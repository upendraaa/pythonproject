import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
tips.head()
# To print the head
# print(tips.head())
# sns.distplot(tips['total_bill'],kde=False,bins=30)

# Joint plot
# sns.jointplot(x= 'total_bill',y='tip',data=tips)

# pair plot
# sns.pairplot(tips,hue= 'sex')

# Rugplot
# sns.rugplot(tips['total_bill'])

# Kde plot
sns.kdeplot(tips['total_bill'])

# To display the plot
plt.show()
