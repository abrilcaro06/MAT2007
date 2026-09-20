# Investigating India's fertility rate over the years 1950 - 2023
### MAT2007, Abril Caro Picas (i6375969)

# Project overview
This project focuses on looking at global fertility rate changes throughout the years of 1950 to 2023. It specifically looks at India, as that is the country that has the highest overall population, and the investigation focuses on the changes throughout the years in the overall expectation of its population growth, with the use of fertility rates as the data points.


# Data source used
The data used for this project was gathered from "Our World in Data", which uses data from the Human Fertility Database (2025) and UN World Population Prospects (2024). 
To retrieve the data used, type India in the search bar, and ensure that the settings is in the table format. Then download the displayed data, which shows to be 19,402 rows. Data is then able to be imported into VS code via the code:

data <- read.csv("https://ourworldindata.org/grapher/children-born-per-woman.csv?v=1&csvType=filtered&useColumnShortNames=true&tab=table&tableSearch=india")
