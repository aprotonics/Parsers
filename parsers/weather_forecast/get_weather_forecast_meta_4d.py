import json
from os import error
import time


day_now = int(time.ctime(time.time()).split(" ")[2].split(":")[0])
time_now = int(time.ctime(time.time()).split(" ")[3].split(":")[0])
time_interval = (time_now - 3) // 6

for i in range(4, 0, -1):

    try:
        file = f"/home/time-traveller/macros/scripts/cdh/weather/weather_new_data_4d_{i}d_{time_interval+1}t.txt"
        weather_data_json = ""

        with open(file=file, mode="rt", encoding="utf-8") as f:
            weather_data_json = f.read()

        weather_data = json.loads(weather_data_json)

        feels_like_temp_str = weather_data["Today"]["feels_like_temp"]
        date = weather_data["Today"]["date"]
        weather_date = date.split(" ")[0].split("-")[2]

        if int(weather_date) == int(day_now):
            print("Weather forecast is up to date")
        else:
            print(f"Weather forecast is by date {weather_date}")

        break

    except OSError:

        continue
