import numpy as np
import pandas as pd
import predictor

data = pd.read_csv('CountryLatLong.csv')

for i in range(len(data)):
    name = data['Country'][i]
    lat = data['Latitude'][i]
    long = data['Longitude'][i]
    pred = predictor.predict([lat, long])

    print('["', end='')
    print(name, end='", ')
    #print(lat, end=', ')
    #print(long, end=', ')
    print(pred, end='],\n')

