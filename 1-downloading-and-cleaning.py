# This script will download and clean the accidents data used in the lab.
# It uses the kaggle API so that user that runs it needs their credentials either stored in the root directory in the privded .json file as a token or the credential information in the .env file.
import os
import requests
import pandas as pd
import kaggle

# We first need to pip install kaggle for the following command to work. This will authenticate us with the Kaggle API so that we can download our data.
kaggle.api.authenticate()

#Finally, I'll import several functions we will use throughout the project from my own python scripts:
from python_scripts import cleaning
from python_scripts import importing

# Using a function I wrote to download the required CSV to our data folder I will download it and import it as a dataframe for further manipulation:
data = cleaning.download_accidents_kaggle()

# The data frame looks pretty clean however, theres some tidying up we can still do:
    # 1. I'll drop the column "weekday" since this column is not very clean and the full date is stored in separate columns.
    # 2. Month_name information is redundant, lets drop this column.
    # 3. The column "weekday_name" just has the names of the days of the week. The full date is stored in separate columns so we will drop this column.
    # 4. Since we wont be using the specific location data for anything, we will drop the columns with coordinates.
data = cleaning.delete_columns(data, ["weekday", "month_name", "weekday_name", "utm_coordinate_y", "utm_coordinate_x", "longitude", "latitude"])

# Lets drop rows with more than 8 Nas, if they exist:
data.dropna(thresh=8)

# Now lets turn the separate columns that make up the date and have a single column with the timestamp as a pandas DateTime column. Since having the date is key for our future analysis, we will first drop any values that have Nans in these columns, this is built in our function.
data = cleaning.make_timestamp(data,["year",  "month",  "day", "hour"])

# With our data set clean and ready to be we processed, we can export it as a clean CSV.
data.to_csv('data/accidents_clean.csv')

## Now lets import weather data to enrich this data base in the next step
# We will be using a free API from open-meteo.com
importing.import_weather_data()
