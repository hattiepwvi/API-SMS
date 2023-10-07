import requests

api_key = "nizhongmezhemekeai"
MY_LAT = 39.904202
MY_LNG = 116.407394
parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
}


response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
data = response.json()
print(data)