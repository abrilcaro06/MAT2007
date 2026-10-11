#must gather the data that is stored in cvs "india_data.csv"

# for this we need pandas, numpy, and matplot.pyplot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file using pandas
df = pd.read_csv('india_data.csv') #loads file into dataframe

# Make the columns
year= df['year'] # adding this plus line below shows that the x values start still at 1950 visually, but on code 1950 is still N0
x = year - 1950 #ensures start of N0=1950
y = df['fertility_rate_hist']

#Plotting scatterplot

plt.figure(figsize=(10,5))
plt.scatter(x, y, label='Data') #this creates the scatterplot
#plt.plot(x, y_fit, color='red', label=f'Linear fit (slope = {slope:.3f})') #this draws line ontop of scatter
#label feed the legend, and the f-string puts the slope value in the label

#Adding the titles and lables
plt.title("Fertility Rate in India over the years 1950-2023")
plt.xlabel('Year')
plt.ylabel('Fertility rate (births per woman)')
plt.legend()
plt.grid(True)

#Save and show
plt.savefig('fertility_scatter.png')
plt.show()



#Plotting Linear regression

#Using linear regression to see relationship between the years, and fertility rates.
#formula -> y= mx+b
# m is the slope. calculated by: 
#b is the y intercept
#Instead of just making it read the years, making intial value 1950. If not it was giving equation y=-0.064x +131, as not taking 1950 as plot 1, rather going to x=0

slope, intercept = np.polyfit(x,y, 1) #this does the linear regression. 1 is the polynomial degree (straight line)

#calculating the slope
m = np.sum((x-np.mean(x)) * (y-np.mean(y))) / np.sum ((x-np.mean(x)) ** 2)
print(m) #when printing slope got value -0.0636... -> -0.064

#calculating the intercept
b = np.mean(y) - m * np.mean(x)
print(b) #the given slope is 130.66

#using line to compute y values for every x
y_fit = slope * x + intercept
print(f"Line of best fit: y = {m:.4f}x + {b:.4f}")

#checkking the correlation coefficiency
r = np.corrcoef(x, y)[0, 1]
print(f'Correlation coefficient r = {r:.3f}')

#creating a plot
plt.figure(figsize=(10,5))
plt.scatter(year, y, label='Data') #this creates the scatterplot
plt.plot(year, y_fit, color='red', label=f'Linear fit (slope = {slope:.3f})') #this draws line ontop of scatter
#label feed the legend, and the f-string puts the slope value in the label

#Adding the titles and lables
plt.title("Fertility Rate in India over the years 1950-2023")
plt.xlabel('Year')
plt.ylabel('Fertility rate (births per woman)')
plt.legend()
plt.grid(True)

#Save and show
plt.savefig('fertility_linebestfit.png')
plt.show()


#Prediction for 1950-2020 worked to predict 2023 accuratly so the equation can now be used to predict 2050.
#Please see the second code "Projectplotting-2020.py" for the previous prediction.

#prediciton of 1950-2020 with other function
year_2023 = (-0.0637 * 73)+6.5546
#note that code takes 1950 as N0, so 2023 = 73, and 2050 = 100

year_2050 = (-0.0636 * 100) + 6.5524
print(f"Predicted fertility rate for 2050 = {year_2050:.3f}")



#Finding mean,varience std, distribution, uncertainty,ect. 

#Finding mean and standard deviation
mean= np.mean(y) #y here represents the fertility rates, as that was defined in line 14

std = np.std(y, ddof =1) #ddof = 1 represents degrees of freedom correlation

print(f"Mean = {mean:.3f}")
print(f"Standard deviation = {std:.3f}") 
