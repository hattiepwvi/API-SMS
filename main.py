import requests
import vonage

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "nizhongmezhemekeai"

weather_params = {
    "lat": 39.904202,
    "lon": 116.407394,
    "appid": api_key,
}

# https://api.openweathermap.org/data/2.5/forecast?lat=39.904202&lon=116.407394&appid=nizhongmezhemekeai

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False

weather_slice = weather_data["list"][0:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# 避免每个小时都 print
if will_rain:
    client = vonage.Client(key="nizhongmezhemekeai", secret="nizhongmezhemekeai")
    sms = vonage.Sms(client)

    responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": "861nizhongmezhemekeai",
            "text": "It's going to rain today. Remember to bring an 🏖️",
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

