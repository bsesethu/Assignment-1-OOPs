# Tab was behaving weirdly here
import pandas as pd
import numpy as np

# Converting '.txt' to '.csv'
# input_file = 'student_habits_performance_comma.txt'
# output_file = 'student_habits_performance_commas.csv'

# df1 = pd.read_csv(input_file, sep= '\t')
# df1.to_csv(output_file, index= False) 

# Read the CSV
# df = pd.read_csv('student_habits_performance_commas.csv')
# print(df)

# Read CSV with delimiter (;)
df2 = pd.read_csv('student_habits_performance.csv', delimiter= ';')
print(df2)  
        # All the issues I was facing are now irrelevant, the string formatting issue I was seeing. I suppose sting values don't need to be in quotations
print(df2.columns)

# Creating a DataLoader class that handles file I/O and exceptions
class DataLoader_IO_n_Excep:
    def __init__(self, file_name):
        self.file_name = file_name
        
    # Error handling where file being loaded is not CSV format
    def __format__(self):
        try:
                
