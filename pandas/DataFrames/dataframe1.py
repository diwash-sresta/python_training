import pandas as pd
data = {"Name" : ["Alice","Bob","Charlie"],
        "Age" : [25,30,35],
        "City": ["NewYork", "Los Angeles","Chicago"]
        }
df = pd.DataFrame(data)
print(df)

# writing a dataframe to a csv file
df.to_csv ("E:\python traiing\pandas\DataFrames\data2.csv", index = False)

name = df["Name"]
print(name)

subset = df[["Name","Age"]]
print(subset)

# sorting by column 
sorted_df = df.sort_values(by="Age",ascending= False)
print(sorted_df)

# grouping by a column
grouped_df = df.groupby("Age").mean()
print(grouped_df)