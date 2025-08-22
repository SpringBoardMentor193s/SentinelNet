import pandas as pd

data=pd.read_csv("../data/nsl-kdd/KDDTrain+.txt")

df=pd.DataFrame(data)
print(df.head())
print(df.info())
print(df.describe())
