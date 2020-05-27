import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv('df1', index_col=0)
print(df1.head())

df2 = pd.read_csv('df2')
print(df2.head())

# df1.hist(['A'])
# OR
# df1['A'].hist()

# df2.plot.area()
# Line graph
df1.plot.line(x=df1.index, y='B')

plt.show()
