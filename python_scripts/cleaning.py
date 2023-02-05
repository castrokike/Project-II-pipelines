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

def make_timestamp (df, date_columns):
    df = df.dropna(subset=date_columns)
    df["date"] = pd.to_datetime(df[date_columns])
    df.drop(columns = date_columns, axis= 1, inplace=True)
    print("Deleted columns: ", list(date_columns), "\nCreated new column 'date' with timestamp based on these columns","\n\n Date range information:")
    print("Max date: ", df["date"].max())
    print("Min date: ", df["date"].min())
    print("Date range: ", df["date"].max() - df["date"].min())

    return df