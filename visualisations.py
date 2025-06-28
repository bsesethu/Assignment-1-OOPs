import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from cleaning_script import DataCleaner_Ass1

df = pd.read_csv('student_habits_performance.csv', delimiter= ';') 
# Clean the dataframe and find the characteristics
clean1 = DataCleaner_Ass1
df = clean1.parentalNulls_fix(df)
print(df.info())

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


# Histogram of study time distibution
Vis = VisualizationEngine
column_name = 'study_hours_per_day'
x_label = 'Study Time (Hours)'
y_label = 'Number of Students'
histo_1 = Vis.histogram(df, column_name, 24, x_label, y_label)

# Skatter plot of sleep vs final scores
col_1 = 'sleep_hours'
col_2 ='exam_score'
skatter_1 = Vis.scatterPlot(df, col_1, col_2)

# Box plots of scores by diet quality
boxplot_1 = Vis.boxplots(df, 'diet_quality', 'exam_score')


