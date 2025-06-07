import json


file = "/home/time-traveller/macros/scripts/cdh/weather_new_data_1d.txt"

weather_data_json = ""

with open(file=file, mode="rt", encoding="utf-8") as f:
    weather_data_json = f.read()


weather_data = json.loads(weather_data_json)

feels_like_temp_str = weather_data["Today"]["feels_like_temp"]
date = weather_data["Today"]["date"]

print("Today's weather")
print(feels_like_temp_str)
print(date)
print()

feels_like_temp_str = weather_data["Tomorrow"]["feels_like_temp"]
date = weather_data["Tomorrow"]["date"]

print("Tomorrow's weather")
print(feels_like_temp_str)
print(date)
print()
