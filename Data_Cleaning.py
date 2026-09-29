import pandas as pd
df= pd.read_csv("credits.csv")

print(df.head())
print("Displayed first 5 rows")

print(df.shape)
print("Showed number of rows and columns")

print(df.columns)
print("Showed all colunm names")

print(df.info())

print(df.describe())
print("View Summary")

print(df.describe(include="object"))
print("Summarize Text Columns")

print(df.duplicated().sum())
print("Count the duplicated vlaues in eah columns")

print(df.isnull().sum())
print("Count the missing values in each column")

print(df.memory_usage(deep= True))
print("Memory usage in all columns")

text_columns = df.select_dtypes(include=["object", "string"]).columns

for col in text_columns:
    df[col] = df[col].str.strip()

print(df["name"].head())

print(df["role"].unique())

print(df["character"].head(20))

print(df[df["character"].isnull()].head(10))

print(df.duplicated(subset=["person_id", "id", "role"]).sum())

print(df[df.duplicated(subset=["person_id", "id", "role"], keep=False)].head(20))

print(df[df.duplicated(keep=False)])

df.to_csv("credits_cleaned.csv", index=False)
print("Credits dataset cleaned successfully!")