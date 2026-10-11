import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('india_data.csv')

# training data to see if doing 1950-2020 data can then accurately predict 2023.
#If this works, then can use my original plot line to predict 2050.

train = df[df['year'] <= 2020]

year = train['year']
y = train['fertility_rate_hist']

# Make 1950 = 0
x = year - 1950

# Linear regression
slope, intercept = np.polyfit(x, y, 1)

print(f"Slope = {slope:.4f}")
print(f"Intercept = {intercept:.4f}")
#results give formula: y= mx+b
#slope (m) = -0.637
#intercept = 6.5546
#formula for 1950-2020 -> y= -0.0637x + 6.5546


#note that the values for my original data
# "ProjectPlotting.py" looking at 1950-2023 has equation:
# y= -0.0636x + 6.5524

#predicting 2023 using y= -0.0637x + 6.5546

year_2023 = (-0.0637 * 73)+6.5546
print(year_2023)


#Get actual 2023 value
actual_2023 = df.loc[df['year'] == 2023, 'fertility_rate_hist'].iloc[0]

print(f"Predicted fertility rate for 2023 = {year_2023:.3f}")
print(f"Actual fertility rate for 2023 = {actual_2023:.3f}")

difference = actual_2023 - year_2023

print(f"Difference = {difference:.3f}")


