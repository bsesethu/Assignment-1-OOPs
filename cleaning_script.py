import pandas as pd
import numpy as np

# Creating a DataLoader class that handles file I/O and exceptions
print('\nPhase 1: Data Loading and Preprocessing')
class DataLoader_IO_n_Excep:
    def __init__(self, file_name):
        self.file_name = file_name
        
    # Error handling check whether file being loaded is of CSV format
    def format_check(self): # Does it have to be a private method. I think so, student_id is personal and can be linked to an individual student. Although we are just checking file format.
        try:
            if self.file_name[-4:] != '.csv':
                return 'Invalid file format used, please input a CSV format file'
            else:
                return self.file_name, ' Correct format detected'
        except TypeError:
            return 'Invalid file, please provide a valid file'      # Maybe do more of these..?
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    

# Implement a datacleaner class to:
class DataCleaner_Ass1:
    # Part of Validation process
    def check_emptyDataFrame(df): # Check of an empty dataframe, hence an empty CSV file
        if(df.empty):
            print('Empty DataFrame, empty CSV file') 
        else:
            print('DataFrame, CSV file nt empty')
        return df
    
    # Check for missing values
    def check_missing(df):
        df_check = df.isna()
        count1 = 0 # To count the number of missing and non missing values
        count2 = 0
        for col in df_check.columns:
            for row in df_check[col]:
                if row == True: # Returns a missing value
                    count1 += 1
                    # print(row, col) # Shows where the None values are. NOTE They are in the 'parental_education_level'
                else:
                    count2 += 1# Returns a non missing value
        print('Number of missing values', count1)
        print('Total number of values in the table', count1 + count2)

        missing_percentage = 100.0 * count1 / (count1 + count2)
        print(f'Proportion of missing data to the total: {round(missing_percentage, 2)}% of data is missing.') # percentage is well below 1%, Unlikely to have a major impact on overall findings
        # print(df.isna()) # Returns missing values as true
        
    def parentalNulls_fix(df): # Rename null/'None' values in 'parental_education_level' column to 'No Education' 
        rows_total = df.shape[0] # Total number of rows

        for i in range(rows_total):
            if pd.isna(df.loc[i, 'parental_education_level']): 
                df.loc[i, 'parental_education_level'] = 'No Education'
        return df
        # Could've done all this using one line
        # df['parental_education_level'].fillna('No Education', inplace= True)

    # Remove duplicates
    def dropDuplicates(df):
        df_noDuplicates = df.drop_duplicates() # Removes any row that is a duplicate of any other, leaving obly the first occurance
        return df_noDuplicates
    
    # Validate data ranges
    def dataTypes(df): # return the datatypes of each column
        return df.dtypes
    
        # Validate, check for negative values where applicable
    def check_negatives(df, column_name):
        has_negative = (df[column_name] < 0).any()
        return has_negative
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Using the DataLoader_IO_n_Excep class
print('\n')
print('Checking file format from file name')
fileName_1 = 'student_habits_performance.csv'
file_test = DataLoader_IO_n_Excep(fileName_1)
print(file_test.format_check())

# Create DataFrame from 'student_habits_performance.csv'
# Read CSV with delimiter (;)
df = pd.read_csv('student_habits_performance.csv', delimiter= ';') # Values in the file are seperated by delimiter ';'. Hence the file is now readable as a df.
print('\n')
print('Original DataFrame, first 5 rows:')
print(df.head())  
        # All the issues I was facing are now irrelevant, the string formatting issue I was seeing. I suppose sting values don't need to be in quotations
print('\n')
print('Columns:')
print(df.columns) # Print column names
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Using the DataCleaner_Ass1 class
print('\nCheck for missing values:')
clean_1 = DataCleaner_Ass1
clean_1.check_missing(df)

# Line 40 is how we find where the null/None values are, in the 'parental_education_level' column.
# Replacing None values with the value 'No Education'
clean_1.parentalNulls_fix(df) # Should return a null free dataframe
# To check whether it's really null free:
print('\nCheck DataFrame after replacing Null/None values')
clean_1.check_missing(df)

# Removing duplicates
print('\nDataFrame after removing duplicate rows, of which there were none (showing first 5 rows):')
df_duplicateFree = clean_1.dropDuplicates(df)
print(df_duplicateFree.head()) # Result says there are zero duplicates in the original df. Number of rows before are equal to the number of rows after

print('\nDatatypes for each column:')
print(clean_1.dataTypes(df))

# Check negatives. Check each number value column individually
print('\n')
print(f'Column {"'exam_score'"} contains negative values: {clean_1.check_negatives(df, 'exam_score')}') # Result is False, meaning there are no negetaive values. NOTE I checked all of them, there are no negative values
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Phase 1 Complete