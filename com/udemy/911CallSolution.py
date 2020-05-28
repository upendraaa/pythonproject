import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('911.csv')

print(df.info())

print(df['title'].iloc[0])
print(df['title'].iloc[0].split(":"))

print(df['title'].apply(lambda title: title.split(":")[0]))
df['reason'] = df['title'].apply(lambda title: title.split(":")[0])
print(df['reason'].value_counts())

sns.countplot(x='reason', data=df)

plt.show()
