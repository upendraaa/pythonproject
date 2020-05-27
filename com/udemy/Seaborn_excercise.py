import matplotlib.pyplot as plt
import seaborn as sbn

sbn.set_style('whitegrid')
titanic = sbn.load_dataset('titanic')

# show distributed chart
# sbn.jointplot(x= 'fare',y= 'age',data=titanic)

# show fare distributed plot
# sbn.distplot(titanic['fare'])

# KDE distributed graph
# sbn.distplot(titanic['fare'],kde=False,color='red')

# Box plot
# sbn.boxplot(x= 'class',y='age',data=titanic,palette='rainbow')

# Swarm plot
# sbn.swarmplot(x= 'class',y = 'age',data=titanic,palette='rainbow')
# Count plot
# sbn.countplot(x='sex',data=titanic)

# Face grid
face = sbn.FacetGrid(data=titanic, col='sex')
face.map(plt.hist, 'age')

print(titanic.head())
plt.show()
