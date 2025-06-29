from sklearn.linear_model import LinearRegression
import pandas as pd
from cleaning_script import DataCleaner_Ass1

df = pd.read_csv('student_habits_performance.csv', delimiter= ';') 
# Clean the dataframe and find the characteristics
clean1 = DataCleaner_Ass1
df = clean1.parentalNulls_fix(df)
print(df.info())

class ScorePredictor:
    # (Function) Convert specific string value to an integer using kwargs. Hence we can then include string value coulumns in the model
    def string_to_Int(self, df, column_name, **kwargs):
        for i, value in enumerate(kwargs.values(), start= 1):
            df.loc[df[column_name] == value, column_name] = i
        return df

Sco = ScorePredictor() #NOTE The round bracet thing is instantiating the variable 'self'.
new_df = Sco.string_to_Int(df, 'gender', arg1='Female', arg2='Male', arg3= 'Other') # String to integer the gender column, do the same to the other string columns
new_df = Sco.string_to_Int(new_df, 'part_time_job', arg1='No', arg2='Yes', arg3= 'Other')
new_df = Sco.string_to_Int(new_df, 'diet_quality', arg1='Good', arg2='Fair', arg3= 'Poor', arg4= 'Other')
new_df = Sco.string_to_Int(new_df, 'parental_education_level', arg1='Master', arg2='High School', arg3= 'Bachelor', arg4= 'No Education')
new_df = Sco.string_to_Int(new_df, 'internet_quality', arg1='Average', arg2='Poor', arg3= 'Good', arg4= 'Other')
new_df = Sco.string_to_Int(new_df, 'extracurricular_participation', arg1='No', arg2='Yes', arg3= 'Other')

print(new_df.head())
                

x = new_df[['age', 'gender', 'study_hours_per_day', 'social_media_hours', 
        'netflix_hours', 'part_time_job', 'attendance_percentage', 
        'sleep_hours', 'diet_quality', 'exercise_frequency', 
        'parental_education_level', 'internet_quality', 'mental_health_rating', 
        'extracurricular_participation']]

# x1 = pd.DataFrame([{ # Trying to imput manually, see if there's a difference. Nope!
#     'age': 23, 'gender': 1, 'study_hours_per_day': 1.0, 'social_media_hours': 3.9, 
#         'netflix_hours': 1.0, 'part_time_job': 1, 'attendance_percentage': 71.0, 
#         'sleep_hours': 9.2, 'diet_quality': 3, 'exercise_frequency': 4, 
#         'parental_education_level': 1, 'internet_quality': 3, 'mental_health_rating': 1, 
#         'extracurricular_participation': 2
# }])
y = new_df['exam_score']

model = LinearRegression() # Needs round brackets, whereas DataCleaner_Ass1 doesn't
model.fit(x, y)

prediction_1 = model.predict(x)[3]
print(prediction_1) # Prediction is the same, with or without the string value columns. How is that possible!?

# print(new_df.info())


# Program to check the number of string variables in the df
# columns_1 = new_df.columns
# cnt = 0
# for col in columns_1:
#     # new_value1 = 0
#     old_value1 = 0
#     for row in df[col]:
#         if isinstance(row, (int, float)) == False: # Check for all non numeric values, i.e string values
#             cnt += 1
# print(cnt)
                
            

