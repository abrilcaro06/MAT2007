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
To retrieve the data used, enter "India" in the search bar of the link above, and ensure that the settings are in the table format. Then download the displayed data, which shows to be 19,402 rows. 
The data can then be imported into VS Code, and the file name is "children-born-per-woman.csv"

# Code
The code that is used is added to the GitHub repository. The code was seperated into two parts.
Part 1 includes the recruitment and analysis of the data. This is seen in "Project.R" in Github. This code fetches the data from the downloaded "children-born-per-woman.csv" file, filters data to only look at India entity, and saves the data in new file, named "india_data.csv".
Part 2 includes the second file in the repository labeled as "ProjectPlotting.py". In this file, the "india_data.csv" is read and plotted using Python. 



# Results
<img width="1000" height="500" alt="fertility_scatter" src="https://github.com/user-attachments/assets/a668b4cb-c59f-4807-92c6-4fbf2592cd33" />
The initial lotting between the years and their corresponding fertility rates can be seen above. 
This was then used to add a line of best fit, done so by a linear regression, which has the formula defined as: y=mx+b. Where m stands for the slope value, and b stands for the y-intercept. Using this equation allows the relationship between the years and the fertility rates to be analyzed, and also allows for future values to be predicted. 


# Sources used
Our World in Data. (2025). Fertility rate: Births per woman. Retrieved September 20, 2026, from https://ourworldindata.org/grapher/children-born-per-woman?tab=table&tableSearch=india

Shankar, P. (2026, June 9). India’s fertility rate falls below replacement level: Why it matters. Al Jazeera. https://www.aljazeera.com/news/2026/6/9/indias-fertility-rate-falls-below-replacement-level-why-it-matters


