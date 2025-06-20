import pandas as pd
import numpy as np

df = pd.read_csv('student_habits_performance.csv', delimiter= ';') # Values in the file are seperated by delimiter ';'. Hence the file is now readable as a df.
# df_check = df.isna()
# count1 = 0
# count2 = 0
# for col in df_check.columns:
#     for row in df_check[col]:
#         if row == True:
#             count1 += 1
#             # print(row, col) # Shows where the None values are. They are in the 'parental_education_level'
#         else:
#             count2 += 1
# print('Number of missing values', count1)
# print('Total number of values in the table', count1 + count2)

# missing_percentage = 100.0 * count1 / (count1 + count2)
# print(f'Proportion of missing data to the total: {round(missing_percentage, 2)}% of data is missing.') # percentage is well below 1%, Unlikely to have a major impact on overall findings

# print(df.isna()) # Returns missing values as true
#-------------------------------------------------------------------------------------------------------------------------------------------------
rows_total = df.shape[0] # Total number of rows
print(rows_total)

# for i in range(rows_total):
#     if pd.isna(df.loc[i, 'parental_education_level']): #NOTE It doesn't want you to say '== None'. Which makes sence, it's not a number. Relic of older code, but the importance of the Note remains    
#         df.loc[i, 'parental_education_level'] = 'No Education'
# Could've done all this using one line
df['parental_education_level'].fillna('No Education', inplace= True)

df.loc[[0], ['parental_education_level']] = 'No Education'
print(df.loc[[0], ['parental_education_level']]) # It works here!! Why did this work, but in the for loop it didn't, I get why though, it's just here that I dont get.


# Dropping duplicates
df.drop_duplicates('parental_education_level')


# Checking if the dataframe has changed
df_check = df.isna()
count1 = 0
count2 = 0
for col in df_check.columns:
    for row in df_check[col]:
        if row == True:
            count1 += 1
            # print(row, col) # Shows where the None values are. They are in the 'parental_education_level'
        else:
            count2 += 1
print('Number of missing values', count1)
print('Total number of values in the table', count1 + count2)

missing_percentage = 100.0 * count1 / (count1 + count2)
print(f'Proportion of missing data to the total: {round(missing_percentage, 2)}% of data is missing.') # percentage is well below 1%, Unlikely to have a major impact on overall findings


# print('\nFind Indexes of missing values')
# result_1 = df['parental_education_level'].isnull().to_numpy().nonzero()
# print(result_1) # Works perfectly, just a bit extra, dont need to include it

