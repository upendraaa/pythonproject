import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df3 = pd.read_csv('df3')
print(df3.info())
print(df3.head())

# Scatter graph, stretch via fig size
# df3.plot.scatter(x= 'a',y='b',color ='red',figsize =(12,3),s = 20)

# Show histagram with column a
# df3['a'].plot.hist()
# plt.style.use('ggplot')

# Box plot for a and b
df3[['a', 'b']].plot.box()

# ix graph
# print(df3.ix[0:30])
df3.ix[0:30].plot.area()

plt.show()
