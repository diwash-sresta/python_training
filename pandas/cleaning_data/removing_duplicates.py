import pandas as pd

df = pd.read_csv('E:\python traiing\pandas\cleaning_data\empty_data.csv')

df.duplicated() 
df.drop_duplicates(inplace = True)
print(df.to_string())