import pprint

import requests

api_key = "f4d43873e9224b91a9bd8210d1edfead"
prefix_url = "http://api.openweathermap.org/data/2.5/weather?"
city = "Sydney"
url = prefix_url + "appid=" + api_key + "&q=" + city


def get_params():
    response = requests.get(url)

    weather = response.json()
    pprint.pprint(weather)

    main = weather["main"]
    temp = main["temp"]
    pressure = main["pressure"]
    humidity = main["humidity"]
    try:
        precipitation = weather["rain"]
    except:
        precipitation = 0

    return temp, pressure, humidity, precipitation
