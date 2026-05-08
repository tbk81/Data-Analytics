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
# print(df.tail(n=1))

# get the last row of data in different ways
# subset_loc = df.loc[0]
# subset_head = df.head(n=1)

# type using loc of 1 row
# print(type(subset_loc))

# type of using head of 1 row
# print(type(subset_head))

# subset columns with loc
# note the position of the colon
# it is used to select all rows
# year_pop_subset = df.loc[:, ['year', 'pop']]
# print(year_pop_subset.head())


# subset columns with iloc
# iloc will allow us to use integers
# -1 will select the last column
# year_pop_subset_iloc = df.iloc[:, [2, 4, -1]]
# print(year_pop_subset_iloc.head())


# create a range of integers from 0 to 4 inclusive
small_range = list(range(0, 5))
print(small_range)

# subset the dataframe with the range
small_subset = df.iloc[:, small_range]
print(small_subset.head())

small_range_two = list(range(3, 6))
small_subset_two = df.iloc[:, small_range_two]
print(small_subset_two.head())

# create a range from 0 - 5 inclusive, every other integer
small_range_three = list(range(0, 6, 2))
small_subset_three = df.iloc[:, small_range_three]
print(small_subset_three.head())





