import requests

urlp1 = 'https://weather.cit.api.here.com/weather/1.0/report.json?product=observation'
latitude = 0.0
longitude = 0.0
urlp2 = '&oneobservation=true&app_id=Yzd1hH5IOppt9cttpCvL&app_code=wiDCHLDcJlt3aUAD8pAJkQ'

url = urlp1 + '&latitude=' + str(latitude) + '&longitude=' + str(longitude) + urlp2
i = 0.0
j = 0.0

while i < 360:
    while j < 360:
        try:
            url = urlp1 + '&latitude=' + str(i) + '&longitude=' + str(j) + urlp2
            res = requests.get(url).json()
            res = res['observations']
            res = res['location'][0]
            print(res['latitude'], end=',')
            print(res['longitude'], end=',')
            hum = res['observation'][0]
            hum = hum['humidity']
            print(hum)
            i = i+1
            j = j+1
        except:
            i = i + 1
            j = j + 1
