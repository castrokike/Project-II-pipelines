# This file declares functions I will use to download and clean my data.
import os
import requests
import pandas as pd
import kaggle
# We first need to pip install kaggle for the following commands to work
kaggle.api.authenticate()


def download_accidents_kaggle():
    os.system(kaggle.api.dataset_download_files('emmanuelfwerr/barcelona-car-accidents', path="data/", unzip=True))

    # The following is a work around for an error I was encountering that did not let me write the file in the /data path.
    # I read the downloaded csv, turn it into a data frame and export the original data to a copy of the original csv in the data path.
    
    data = pd.read_csv('data/accidents_opendata.csv')
    #data = pd.read_csv('accidents_opendata.csv')
    #data.to_csv('data/accidents_opendata.csv')
    #os.remove('accidents_opendata.csv')

    return data