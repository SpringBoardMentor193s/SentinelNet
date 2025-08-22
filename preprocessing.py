import pandas as pd

train_path = r"C:\Users\ASUS\OneDrive\Desktop\Project\Data\KDDTrain+.txt"
test_path = r"C:\Users\ASUS\OneDrive\Desktop\Project\Data\KDDTrain+.txt"

df_train = pd.read_csv(train_path, header=None)
df_test = pd.read_csv(test_path, header=None)

print("Train shape:", df_train.shape)
print("Test shape:", df_test.shape)
