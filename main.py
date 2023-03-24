#using data.csv file predict if we will row based on input
#using logistic regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#get weather data of wilmette illinois 
import requests
import json
import datetime

#api key
#42.0270046,-87.7089185
API_KEY = 'dd1699dbc22718a39aca76f7c9fc26b7'
URL = 'http://api.openweathermap.org/data/2.5/onecall?lat=42.0270046&lon=-87.7089185&exclude=hourly,daily&appid={API_KEY}'

#make request
response = requests.get(URL)
data = response.json()
#get current temp
main = data['main']
#get current weather
weather = main['weather']
#get current wind speed
wind_speed = main['wind_speed']
temp= main['temp']
print(temp, weather, wind_speed)
"""
input will be column 2,3,4 combined and output will be row 1
skip row 0

df = pd.read_csv('data.csv', usecols=[2,3,4,1], skiprows=[0])
print(df)
"""

