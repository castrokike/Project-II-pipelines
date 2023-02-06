# Project II: Pipelines
## Week 3 Project
### Andrés Castro

For this project I used public data from traffic accidents in Barcelona and added weather information for the exact time of the reported time using a free public API. Then I analyzed it to see if the weather conditions could have an impact on the occurance of accidents.

![Alt text](images/Barcelona.jpg)

The data source was fairly clean so data cleaning was minimal (deleted a few columns and hardly dropped any rows for lack of values). 

The main hypothesis I tried to prove was:

## Weather variables (temperature, rain, humidity) have an effect on the occurance of traffic accidents

The accidents data was obtained through the Kaggle API. It consisted of a .csv file with 110.682 unique observations of traffic accidents. These observations spanned from 01/01/2010 to 31/12/2021. This dataset included 4 columns with information on the year, month, day and hour of ocurrance. These columns were mereged into a single DateTime pandas column.

From the [Open Meteo](https://open-meteo.com) free open source weather API I obtained weather information to enrich the accidents dataframe. In a single call I obtained weather information on 9 variables for every hour of every day from 01/01/2010 to 31/12/2021 (~ 105K data points).

With these two data sets I added weather information for the exact reported hour to every accident in the original data set and analyzed correlations:
![Alt text](images/correlation1.jpg)

Seeing these low correlations I thought that maybe grouping by date could increase these relationships. Sadly, the correlations were not greatly affected:
![Alt text](images/correlation2.jpg)

Finally I split my dataset by the incident type and analyzed correlaitons for every type:
![Alt text](images/correlation3.jpg)