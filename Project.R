library(jsonlite)

# Fetch the data
data <- read.csv("https://ourworldindata.org/grapher/children-born-per-woman.csv?v=1&csvType=filtered&useColumnShortNames=true&tab=table&tableSearch=india")


#Ensuring correct structure
#str(data)
#head(data)
#unique(data$entity) #see which country names exist

#names(data)

#Filter to only using India
india <- subset(data, entity == "India")
#print (india) #once wanting to see all of the lines, do this

#checking the column names
print(names(india))
#column names are: "entity", "code", "year", "fertility_rate_hist"

#print(summary(india$fertility_rate_hist)) # to look at the minimum, 1st quarter, median, 3rd quarter, max

#Because i will be using python for the visualization of the data, I will save the results into a new file.

# Save the India data as a CSV file
write.csv(india, "india_data.csv", row.names = FALSE)

#Continuation of plotting in new file
