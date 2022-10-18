import pandas as pd

df = pd.read_excel('Test.xlsx')

# df = pd.read_csv(r'C:\Users\PC\OneDrive\Documents\Usage Report\MatIssuance.csv')

# first 5 rows:
# print(df.head(5))
# particular iloc (index location) ie. iloc 4, this one is great!
# print(df.iloc[4])
# range of iloc (index location) ie. iloc 4, this one is great!
# print(df.iloc[2:4])

#specific cell/location w/reference to iloc, remember 0 based on columns
# print(df.iloc[2,6])

# iterate a loop, and display particular columns
# for index, row in df.iterrows():
	# print(index, row['OrderNo'], row['MatDesc'], row['MatCode'], row['Region'])

#filtering a column given a criteria:
# print(df.loc[df['JobType']=="Install"])

#sorting
# print(df.sort_values(['GPON Compliance', 'PostingDate'], ascending = [1,0]))

# # adding a total column and get the total of each columns. the added column is not on the actual file
# df['Total'] = df['tuguegarao']+df['lion']+df['sugar']+df['milk']+df['potato']+df['alcohol']+df['baclaran']
# print("before:")
# print(df.head(5))
# #delete the 'total' column previously on the data frame
# df = df.drop(columns=['Total'])
# print("after:")
# print(df.head(5))
#more interesting way of adding a total column and get the total of each columns
df['Total'] = df.iloc[:,0:7].sum(axis=1)  #1 is horizontal , 0 = vertical
print(df.head(5))


#statistics figures
# print(df.describe())


#to printthe header columns
# print(df.columns)
# read just one particular column all rows
# print(df['AcctNo'])

# read just one particular column but particular rows only
# print(df['MatDesc'][:80])

# choose specific columns only
# print(df[['MatDesc', 'MatType', 'SLI Partner', 'job_desc']])
