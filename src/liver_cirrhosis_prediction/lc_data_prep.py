import pandas as pd     # type: ignore

data = pd.read_csv('src/liver_cirrhosis_prediction/cirrhosis.csv')

print(data.head())
