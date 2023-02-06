# This script has functions I will use to import weather data from the Open Meteo API. The funcitons declared here will be called by the "1-downloading-and-cleaning.py" script in this repo.
import requests
import pandas as pd

## Function declaration

def import_weather_data():
    """
    This function takes no arguments, it is written to automate the process of requesting weather info from the open-meteo API for the timeframe of the Accidents database.
    It also splits the response into an hourly database and a daily database.
    """
    # We first get the desired weather data from the Open Meteo API
    url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.40&longitude=2.17&start_date=2010-01-01&end_date=2021-12-31&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,precipitation,rain,windspeed_100m,winddirection_100m,soil_temperature_100_to_255cm,soil_moisture_100_to_255cm&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,apparent_temperature_max,apparent_temperature_min,apparent_temperature_mean,sunrise,sunset,precipitation_sum,rain_sum,precipitation_hours&timezone=Europe%2FBerlin"
    response = requests.request("GET", url)
    weather_data = pd.DataFrame(response.json())

    # Now we process the response to get clean hourly and daily weather information.
    weather_data_hourly = pd.DataFrame([weather_data["hourly"][range(10)]])
    weather_data_hourly = weather_data_hourly.apply(lambda x: x.explode())

    # We have the desired hourly information, but the timestamp column it includes is not exactly a pandas DateTime column. We need to process it further:
    weather_data_hourly["hour"] = weather_data_hourly["time"].apply(lambda x: int(x.split("T")[1].split(":")[0]))
    weather_data_hourly["day"] = weather_data_hourly["time"].apply(lambda x: int(x.split("T")[0].split("-")[2]))
    weather_data_hourly["month"] = weather_data_hourly["time"].apply(lambda x: int(x.split("-")[1]))
    weather_data_hourly["year"] = weather_data_hourly["time"].apply(lambda x: int(x.split("-")[0]))
    weather_data_hourly["date"] = pd.to_datetime(weather_data_hourly[["year", "month", "day", "hour"]])
    weather_data_hourly[["time", "year", "month", "day", "hour", "date"]]
    weather_data_hourly.drop(["time", "year", "month", "day", "hour"], axis = 1, inplace=True)
    
    # Now lets do the same thing but for the daily data. For this we need the first row, and then a range of the last rows. lets create this list first
    columns_=[0]
    for i in list(range(10,21)):
        columns_.append(i)

    weather_data_daily = pd.DataFrame([weather_data["daily"][columns_]])
    weather_data_daily = weather_data_daily.apply(lambda x: x.explode())

    # We have to repeat the process of transforming the timestamp, although this time we have to slightly tune it because we do not want the hour information.
    weather_data_daily["day"] = weather_data_daily["time"].apply(lambda x: int(x.split("-")[2]))
    weather_data_daily["month"] = weather_data_daily["time"].apply(lambda x: int(x.split("-")[1]))
    weather_data_daily["year"] = weather_data_daily["time"].apply(lambda x: int(x.split("-")[0]))
    weather_data_daily["date"] = pd.to_datetime(weather_data_daily[["year", "month", "day"]])
    weather_data_daily[["time", "year", "month", "day", "date"]]
    weather_data_daily.drop(["time", "year", "month", "day"], axis = 1, inplace=True)
    
    #Finally, we'll export these two data sub-sets:
    weather_data_daily.to_csv('data/daily_weather.csv')
    weather_data_hourly.to_csv('data/hourly_weather.csv')

    return