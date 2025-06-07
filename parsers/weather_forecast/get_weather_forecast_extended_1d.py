import json


file = "/home/time-traveller/macros/scripts/cdh/weather_data_1d.txt"

weather_data_json = ""

with open(file=file, mode="rt", encoding="utf-8") as f:
    weather_data_json = f.read()


weather_data = json.loads(weather_data_json)

weather_temp = weather_data["Today"]["temperature"]
humidity = weather_data["Today"]["humidity"]
wind_speed = weather_data["Today"]["wind_speed"]
feels_like_temp_str = weather_data["Today"]["feels_like_temp"]
date = weather_data["Today"]["date"]

print("Today's weather")
print(f"Temperature {round(weather_temp)} Celsius")
print(f"Humidity {humidity} %")
print(f"Wind speed {round(wind_speed)} m/s")
print(feels_like_temp_str)
print(date)
print()


weather_temp = weather_data["Tomorrow"]["temperature"]
humidity = weather_data["Tomorrow"]["humidity"]
wind_speed = weather_data["Tomorrow"]["wind_speed"]
feels_like_temp_str = weather_data["Tomorrow"]["feels_like_temp"]
date = weather_data["Tomorrow"]["date"]

print("Tomorrow's weather")
print(f"Temperature {round(weather_temp)} Celsius")
print(f"Humidity {humidity} %")
print(f"Wind speed {round(wind_speed)} m/s")
print(feels_like_temp_str)
print(date)
print()
