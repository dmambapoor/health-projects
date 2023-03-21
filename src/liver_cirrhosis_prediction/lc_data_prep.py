import pandas as pd     # type: ignore

data = pd.read_csv('src/liver_cirrhosis_prediction/cirrhosis.csv')

print(data.head())

for col in data.columns:
    print(data[col].isnull().value_counts())
