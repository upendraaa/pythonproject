import pandas as pd

# Read Salaries CSV
sal = pd.read_csv("D:\python\Salaries.csv")
print(sal)

# 2:
print(sal.head())

# 3: Info
print("Info")
print(sal.info())

# 4: Average Base pay
print("Average base pay")
# average = sal['BasePay'].mean()
# print("{}".format(average))
