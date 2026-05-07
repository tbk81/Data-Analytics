import pandas as pd

df = pd.read_csv('./data/gapminder.tsv', sep='\t')
# print(df)

# check data type i.e., a dataframe
# print(type(df))

# retrieves the number of rows and columns
# print(df.shape)

# get column names
# print(df.columns)

# get the dtype of each column
# print(df.dtypes)

# get more information about our data
# print(df.info())

# show the first 5 observations
# print(df.head())

# just get the country column and save it to its own variable
# country_df = df['country']
# print(country_df.head())
# print(country_df.tail())

# Looking at country, continent, and year
# subset = df[['country', 'continent', 'year']]
# print(subset.head())

# using dot notation
# print(df.country.head())

# get the first row
print(df.iloc[0])
# for i in range(10):
#     print(df.iloc[i])

# get last row
num_of_rows = df.shape[0]
last_row_index = num_of_rows - 1
print(df.iloc[last_row_index])

# another way to get the last row
print(df.tail(n=1))

# get the last row of data in different ways
subset_loc = df.loc[0]
subset_head = df.head(n=1)

# type using loc of 1 row
print(type(subset_loc))

# type of using head of 1 row
print(type(subset_head))


