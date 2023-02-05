# This file declares functions I will use to download and clean my data.
import os
import requests
import pandas as pd
import kaggle
# We first need to pip install kaggle for the following commands to work
kaggle.api.authenticate()


def download_accidents_kaggle():
    """
    This function downloads the CSV file from the dataset "barcelona-car-accidents" from Kaggle using the Kaggle API. It then uses pandas to read the CSV and returns the corresponging DataFrame.
    """
    os.system('kaggle datasets download -d emmanuelfwerr/barcelona-car-accidents --unzip --p "data/"')
    data = pd.read_csv('data/accidents_opendata.csv')

    return data

def delete_columns (df, columns):
    """
    This function takes a data frame a list of specific columns and deletes those columns form the dataset. It returns the same dataset without the columns specified.
    """
    df.drop(columns = columns, inplace=True)
    print("Deleted columns: ", list(columns))
    
    return df