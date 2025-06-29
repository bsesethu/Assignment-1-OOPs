import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


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
    
    # (Function) Find outlier values and indices of a single column. NOTE it may need to be normally distributed, find out
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
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class VisualizationEngine:
    # (Function) Create a histogram of one of the columns of a dataframe
    def histogram(df, column_name, num_of_bins, xlabel, ylabel): # specify these characteristics of your histogram
        study_time = df[column_name]
        title = 'Histogram of ' + column_name
        plt.hist(study_time, bins= num_of_bins, color= 'skyblue', edgecolor= 'black')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()
    
    # (Function) Create a scatter plot of one column vs another
    def scatterPlot(df, column_name1, column_name2): # Specify these characteristics of your skatter plot
        x = df[column_name1]
        y = df[column_name2]
        title_name = 'Skatter plot of ' + column_name1 +  ' vs ' +  column_name2

        plt.scatter(x, y, alpha= 0.7, cmap= 'viridis', marker= '.')
        plt.xlabel(column_name1)
        plt.ylabel(column_name2)
        plt.title(title_name)
        plt.show()
    
    # (Function) Create boxplots of scores by diet quality
    def boxplots(df, column_1, column_2):
        sns.boxplot(x= column_1, y= column_2, data= df[[column_1, column_2]])
        title_str = 'Box Plot of ' + column_1 + ' by ' + column_2
        plt.title(title_str)
        plt.xlabel(column_1)
        plt.ylabel(column_2)
        plt.show()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class ScorePredictor:
    # (Function) Model function. Linear regression
    def model_LinearReg(self, df, X, prediction_num): # X is the input features, prediction_num is the index of the prediction required
        y = df['exam_score']

        model = LinearRegression() # Needs round brackets, whereas DataCleaner_Ass1 doesn't. Its all about whether or not therre was 'self' in the method parameters.
        model.fit(X, y)

        prediction = model.predict(x)[prediction_num]
        return prediction
   
    # (Function) Convert specific string value to an integer using kwargs. Hence we can then include string value coulumns in the model
    def string_to_Int(self, df, column_name, **kwargs):
        for i, value in enumerate(kwargs.values(), start= 1):
            df.loc[df[column_name] == value, column_name] = i
        return df
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
