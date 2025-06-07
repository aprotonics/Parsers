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

        print("Today's weather")
        print(feels_like_temp_str)
        print(date)
        print()

        weather_data_keys = weather_data.keys()
        weather_data_keys_copy = []

        for value in weather_data_keys:
            weather_data_keys_copy.append(value)

        for i in range(len(weather_data_keys_copy)):
            value = weather_data_keys_copy[i]

            if i > 0:
                feels_like_temp_str = weather_data[value]["feels_like_temp"]
                date = weather_data[value]["date"]

                print(f"{value}'s weather")
                print(feels_like_temp_str)
                print(date)
                print()
        
        break

    except OSError:

        continue
