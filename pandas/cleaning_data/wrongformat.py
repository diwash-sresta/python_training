import pandas as pd

df = pd.read_csv('E:\python traiing\pandas\cleaning_data\empty_data.csv')

df['Date'] = pd.to_datetime(df['Date'], format= "mixed")

print(df.to_string())