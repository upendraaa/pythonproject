import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')
print(iris.head())
print(iris['species'].unique())
# pairplot
# sns.pairplot(iris)

# pair grid
# pg =sns.PairGrid(iris)
# pg.map_diag(sns.distplot)
# pg.map_upper(plt.scatter)
# pg.map_lower(sns.kdeplot)

# Face grid
tips = sns.load_dataset('tips')
g = sns.FacetGrid(data=tips, col='time', row='smoker')
g.map(sns.distplot, 'total_bill')

plt.show()
