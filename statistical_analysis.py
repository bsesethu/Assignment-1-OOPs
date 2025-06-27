import numpy as np
import pandas as pd
from cleaning_script import DataCleaner_Ass1

df = pd.read_csv('student_habits_performance.csv', delimiter= ';') 
# Clean the dataframe and find the characteristics
clean1 = DataCleaner_Ass1
df = clean1.parentalNulls_fix(df)
print(df.head())
print(df.info())
print(df.shape)

class StudentAnalyser:
    #  (Function) Isolate and return only two specific columns from the DF
    def isolateColumns(df, column_name1, column_name2):
        df_condensed = df[[column_name1, column_name2]] # If we are more than one column, we must have double square brackets
        return df_condensed
    
    # (Funtion) Group and calculate various aggregations
    def group_nFind(df, grouped_column, agg): # grouped_column is the column the groupby function is applied to. agg is the choice of aggregation used.
        if agg == 'mean':
            df_grouped = df.groupby([grouped_column]).mean().round(2) 
        elif agg == 'median':
            df_grouped = df.groupby([grouped_column]).median().round(2) 
        return df_grouped
    
    # (Function) Find the standard deviation of a single column
    def isolate_nStd(df, column_name):
        sigma = round(np.std(df[column_name]), 2) # Returns the standard deviation 
        return sigma
    
    # (Function) Find outlier values and indices of a single column
    def findOutliers(df, column_name, sigma): #NOTE Returns two variables, sigma is the standard deviation. 
        mean_value = df[column_name].mean() # Mean value
        print('Mean value:', mean_value)
        
        # Upper and lower boundaries, beyond which we can identify outliers
        upper_b = round(mean_value + (3 * sigma), 2)
        lower_b = round(mean_value - (3 * sigma), 2)
        print('Upper and lower boundaries', upper_b, lower_b) # There are no values for 'social_media_hours' that are less than 0, lower_b is less than that . Hence there won't be any lower bound outliers
        
        # Find outliers
        rows_total = df.shape[0]
        index_val = []
        outlier_val = []
        for i in range(rows_total):
            if df.loc[i, column_name] > upper_b:
                index_val.append(i) # Returns index of outlier
                outlier_val.append(df.loc[i, column_name]) # Returns outlier value
                
            elif df.loc[i, column_name] < lower_b:
                index_val.append(i) # Returns index of outlier
                outlier_val.append(df.loc[i, column_name]) # Returns outlier value
        
        return outlier_val, index_val

    
# Instantiate and find mean/median study time by mental health tier 
StA = StudentAnalyser
df_grouped_1 = StA.isolateColumns(df, 'mental_health_rating', 'study_hours_per_day')

print('\nAverage study hours per day, grouped by mental health rating')
df_grouped_1_mean = StA.group_nFind(df_grouped_1, 'mental_health_rating', 'mean') 
print(df_grouped_1_mean)

print('\nMedian study hours per day, grouped by mental health rating')
df_grouped_1_median = StA.group_nFind(df_grouped_1, 'mental_health_rating', 'median')
print(df_grouped_1_median)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Identify correlation between sleep and exam scores
# Isolate the two columns
df_sl_ex = StA.isolateColumns(df, 'sleep_hours', 'exam_score')
print('\n', df_sl_ex)

# Identify correlation by finding exam_score grouped by sleep time. Best way to do this is to visualize it.. Later
df_sl_ex_grouped = StA.group_nFind(df_sl_ex, 'sleep_hours', 'mean')
print('\n')
print(df_sl_ex_grouped.head())
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Detect outliers in social media usage
sigma = StA.isolate_nStd(df, 'social_media_hours')
print('\nStandard dev. of social media hours', sigma)

# Find outlers
outlier_value, index_value = StA.findOutliers(df, 'social_media_hours', sigma)
print('\nOutlier values:', outlier_value)
print('Outlier index values:', index_value)

# FIN -----------------------------------------------------------------------------------------------------