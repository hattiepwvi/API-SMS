import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "nizhongmezhemekeai"

weather_params = {
    "lat": 39.904202,
    "lon": 116.407394,
    "appid": api_key,
}


response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)