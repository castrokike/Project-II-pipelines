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



# Using a function I wrote to download the required CSV to our data folder I will download it and import it as a dataframe for further manipulation:
data = cleaning.download_accidents_kaggle()

# The data frame looks pretty clean however, theres some tidying up we can still do:
# 1. I'll drop the column "weekday" since this column is not very clean and the full data is in the column "weekday_name"
    #data.drop(["weekday"],axis=1, inplace=True)
# 2. Month_name information is redundant, lets drop this column:
    #data.drop(["month_name"],axis=1, inplace=True)
cleaning.delete_columns(data, ["weekday", "month_name"])
# Finally, lets drop rows with more than 8 Nas, if they exist:
data.dropna(thresh=8)
# Looks like we only dropped one row. Lets export this clean CSV.
data.to_csv('data/accidents_clean.csv')

