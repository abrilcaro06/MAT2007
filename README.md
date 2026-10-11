# Investigating India's fertility rate over the years 1950 - 2023
### MAT2007, Abril Caro Picas (i6375969)

# Project overview
This project investigates the changes that India's fertility rate has undergone throughout the years from 1950 to 2023, with the aim of using this data to predict the rate for the future. India was specifically chosen as it is the country with the highest population worldwide, yet their fertility rate has drastically decreased over the years and have now fallen below the threshold to keep the population stable in the long run (Shankar, 2019).  

## Research Question
How has India's global fertility rate changed from 1950 to 2023, and how can that trend be used to predict rates for 2050?

# Dataset 
The data used for this project was gathered from "Our World in Data", which uses data from the Human Fertility Database (2025) and UN World Population Prospects (2024).

The source used was: [Fertility rate: births per woman] (https://ourworldindata.org/grapher/children-born-per-woman?tab=table&tableSearch=india)

## How to gather the correct data
To retrieve the data used go on Our World in Data into the fertility database. Once the website opens, go to the search bar and enter "India", and ensure that the settings are in the table format. Then click the download button, and only download the displayed data, which includes 19,402 rows. 
The data can then be imported into VS Code, and the file name is "children-born-per-woman.csv"

This data will then need to be filtered through code, seen in **Project.R**, to retrieve 74 lines of code that will be used throughout this research investigation. Out of these 74 data points, 1 line is the headers, while the other 73 are the data points from 1950-2023.

# Code
All of the code used is visible in the GitHub repository. The code was separated into multiple parts.

### Part 1 - Data collection
Part 1 includes the recruitment and analysis of the data. This is seen in **"Project.R"** in Github. This code fetches the data from the downloaded "children-born-per-woman.csv" file, filters data to only look at India entity, and saves the data in new file, named "india_data.csv".


### Part 2 - Plotting scatterplot Data collection
The second part includes creating the scatterplot, which was made in the code file labeled as **"ProjectPlotting.py"**.
In this file, the "india_data.csv" is read and plotted using Python. 
The extensions used were: numpy, pandas and matplotlib
Here, the scatterplots were made, including the line of best fit, the equation, and the r coefficient.
Other values were also coded for, showing the prediction value for 2050 and the mean and standard deviation.

### Part 3 - Calculations for the back-test (1950-2020) 
In this file, the backtest calculations to predict 2023 from data 1950-202 was done. I chose to do this in a new file to have these calculations separated from my main data set to avoid confusion. This file is found under the name **"ProjectPlotting-2020.py"**.

### Part 4 - Subsampling method: Line of best fit and Gaussian distribution 
In this file, I did all the calculations and plotting with the 5 different subgroups. This is found in the repository labeled as **"ProjectSubsampling.py"** 


# Results
<img width="1000" height="500" alt="fertility_scatter" src="https://github.com/user-attachments/assets/a668b4cb-c59f-4807-92c6-4fbf2592cd33" />

The initial plotting between the years and their corresponding fertility rates can be seen above. 
This was then used to add a line of best fit, done so by a linear regression, which has the formula defined as: y=mx+b. Where m stands for the slope value, and b stands for the y-intercept. Using this equation allows the relationship between the years and the fertility rates to be analyzed, and also allows for future values to be predicted. 

<img width="1000" height="500" alt="fertility_linebestfit" src="https://github.com/user-attachments/assets/ff95a621-6afe-4650-898e-c46383944f10" />

This new figure includes the line of best fit, which can now be defined as:

[y= -0.0636x + 6.5524]

The r value was also calculated through the code in "ProjectPlotting.py" and yielded a value of r= -0.985. This correlation coefficient is shown to be a strong negative correlation. 

## Back-testing linear function 
To see if the line of best fit can be accurately used to predict 2050, I took the values for 1950-2020 and created a new linear regression.  
The code for this can be found in the repository: **"Projectplotting-2020.py"**
This gave the equation: y= -0.0637x + 6.5546.
This equation was then used to calculate for the year 2023 and see if it could accurately predict it.
The actual value of 2023 was 1.975, whilst the function predicted 2023 to have a fertility rate of 1.904, leading to a difference of 0.071.


## Predicting 2050 

As this difference is very small, the original function will now be used to predict 2050.
As the function takes 1950 as the initial value, to find 2050, x must be 100.

y= -0.0636(100) + 6.5524
y=0.192

Then the subsampling was done, where the data was split into 5 subgroups, each containing around 14 data points. 
All the subsampling calculations and plotting were done in the **"ProjectSubsampling.py"**

The prediction of 2050 for each group can be found below:


| Group Number.                               | Prediction (Births per woman)   |
| ------------------------------------------  | ------- |
| Group 1                                     | 0.185   |
| Group 2                                     | -0.17   |
| Group 3                                     | 0.426   |
| Group 4                                     | 0.270   |
| Group 5                                     | 0.258   |

The sigma values were also calculated in this code:

| Group Number                               | Sigma range   |
| ------------------------------------------  | ------- |
| 1 sigma (68%)                               | -0.03 to 0.42   |
| 2 sigma (95%)                               |  -0.25 to 0.64   |
| 3 sigma (99.7%)                             | -0.47 to 0.86   |


The overall mean and uncertainty gave a value of 0.19 +/- 0.22, which can be seen in the graph.


<img width="1000" height="500" alt="line5subsample" src="https://github.com/user-attachments/assets/90c7187a-c7a2-4ae9-8168-5933d11fb278" />

- The red line is the line of best fit for 2050 without subsampling 
- Blue lines represent the line of best fit for every subgroup, all extrapolating to 2050.
- Black point is the 2050 value including uncertainty, found by using the 5 subgroups

Then the 5 groups were plotted into a Gaussian distribution, as seen below.

<img width="640" height="480" alt="Gaussiandistribtion" src="https://github.com/user-attachments/assets/0cc4e2f3-06c8-4d29-b67c-fd2f47b1744d" />

- Mean is 0.19 births per woman
- Uncertainty is 0.22
- Red dots represent each subgroup value in the tables above
- 3 subgroups fit the 1 sigma range
- 2 subgroups fit the 2 sigma range

# Conclusion of results

The original linear regression plot presented a predicted value of 0.192 births per woman. When backtesting was conducted, the prediction of 2023 using data from 1950-2020 was only 3.6% off the original value. The method of subsampling was used to get more linear regressions, and all were plotted to extrapolate for 2050 and plot on a Gaussian distribution curve. Showing a value of 0.19 +/- 0.22 births per woman in 2050, which was very close to the original value found through the linear regression equation. These results remain below the benchmark of 2.1 for India to continue having a stable population. Nonetheless, it is important to note that the value for uncertainty was only accounting for the 5 subgroups, and this would change if different values were used. Therefore, the investigation would benefit from further replication of the results to give a more stable sigma value. Furthermore, the results themselves are not very realistic due to the linear model continuously decreasing, leading to values lower than zero, which is not possible. A different model would be a better fit and would likely account for the values from the 1960s better, as those had a slight upward curve in fertility rates, leading to the thought that an S-curve might fit the data set better than the linear regression that was used, this was a model that was used by the UN and predicted a value of 1.76 births per woman. Therefore, if there was more time, a different model could be used, and the results could be compared to the values predicted by the UN for 2050.  



# Sources used
Our World in Data. (2025). Fertility rate: Births per woman. Retrieved September 20, 2026, from https://ourworldindata.org/grapher/children-born-per-woman?tab=table&tableSearch=india

Shankar, P. (2026, June 9). India’s fertility rate falls below replacement level: Why it matters. Al Jazeera. https://www.aljazeera.com/news/2026/6/9/indias-fertility-rate-falls-below-replacement-level-why-it-matters

United Nations. (n.d.). Total Fertility rate. United Nations Data Portal. https://population.un.org/dataportal/data/indicators/19/locations/356/start/2020/end/2050/table/pivotbylocation?df=de99908b-6592-4283-9133-00233b8bbb34



