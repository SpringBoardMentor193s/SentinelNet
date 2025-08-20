import pandas as pd
data = pd.read_csv('../data/KDDTrain+.csv', header=None)
print("Shape of Data: "+ str(data.shape))
print(data.head())
print(data.describe())
print(data.info())