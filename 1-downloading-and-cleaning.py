# This script will download and clean the accidents data used in the lab.
# It uses the kaggle API so that user that runs it needs their credentials either stored in the root directory in the privded .json file as a token or the credential information in the .env file.
import os
import requests
import pandas as pd
import kaggle
# We first need to pip install kaggle for the following commands to work
kaggle.api.authenticate()
from python_scripts import cleaning

'''
# Downloading the data file from kaggle using the kaggle api
!kaggle datasets download -d emmanuelfwerr/barcelona-car-accidents --unzip

# This is a work around for an error I was encountering that did not let me write the file in the /data path.
# I read the downloaded csv, turn it into a data frame and export the original data to a copy of the original csv in the data path.
data = pd.read_csv('accidents_opendata.csv')
data.to_csv('data/accidents_opendata.csv')
os.remove('accidents_opendata.csv')

#Since we already improted the data into a data frame, we dont need to read it again from the new location.

'''
data = cleaning.download_accidents_kaggle()

# The data frame looks pretty clean however, theres some tidying up we can still do:
# I'll drop the column "weekday" since this column is not very clean and the full data is in the column "weekday_name"
data.drop(["weekday"],axis=1, inplace=True)
# Month_name information is redundant, lets drop this column:
data.drop(["month_name"],axis=1, inplace=True)
# Finally, lets drop rows with more than 8 Nas, if they exist:
data.dropna(thresh=8)
# Looks like we only dropped one row. Lets export this clean CSV.
data.to_csv('data/accidents_clean.csv')

