import pandas as pd

df = pd.read_csv('E:\python traiing\pandas\cleaning_data\empty_data.csv')

# df.dropna(inplace = True)
# df.fillna(130, inplace = True)
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)


print(df.to_string())