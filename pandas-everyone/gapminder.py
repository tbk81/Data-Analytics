import pandas as pd

df = pd.read_csv('./data/gapminder.tsv', sep='\t')
# print(df)

# check data type ie a dataframe
print(type(df))

# retrieves the number of rows and columns
print(df.shape)

# get column names
print(df.columns)

# get the dtype of each column
print(df.dtypes)

# get more information about our data
print(df.info())

# show the first 5 observations
print(df.head())

