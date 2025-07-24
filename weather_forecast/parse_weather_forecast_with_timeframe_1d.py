import requests
import json
import time


city_name = "Ekaterinburg"
limit = "10"
API_key = "aeec885008d269549d0981041cfb9499"
url = "https://api.openweathermap.org/geo/1.0/direct"

weather_data = {}
data = ""

def fetch_with_time_out_get(url, city_name, limit, API_key, timeout):
    url = url
    city_name = city_name
    limit = limit
    API_key = API_key
    timeout = timeout

    start = time.time()
    data = ""

    with requests.get(url, params={"q": city_name, "limit": limit, "appid": API_key}, stream=True) as response:
        response.raise_for_status()

        data = bytearray()

        for chunk in response.iter_content(chunk_size=8192):
            if time.time() - start > timeout:
                raise TimeoutError()

            data.extend(chunk)

    return data

def fetch_with_time_out_post(url, latitude, longitude, units, API_key, timeout):
    url = url
    latitude = latitude
    longitude = longitude
    units = units
    API_key = API_key
    timeout = timeout

    start = time.time()
    data = ""

    with requests.post(url, params={"lat": latitude, "lon": longitude, "units": units, "appid": API_key}, stream=True) as response:
        response.raise_for_status()

        data = bytearray()

        for chunk in response.iter_content(chunk_size=8192):
            if time.time() - start > timeout:
                raise TimeoutError()

            data.extend(chunk)

    return data

try:
    data = fetch_with_time_out_get(url, city_name, limit, API_key, 5)
except TimeoutError as err:
    print()
    print()
    print(err)
    print("Time of requesting has exceeded timeout limit")
    print()

response_dict = json.loads(data)

weather_main =  response_dict[0]["name"]
latitude =      response_dict[0]["lat"]
longitude =     response_dict[0]["lon"]


latitude = round(latitude, 2)
longitude = round(longitude, 2)
API_key = "aeec885008d269549d0981041cfb9499"
units = "imperial"
url = "http://api.openweathermap.org/data/2.5/forecast"

try:
    data = fetch_with_time_out_post(url, latitude, longitude, units, API_key, 5)
except TimeoutError as err:
    print()
    print()
    print(err)
    print("Time of requesting has exceeded timeout limit")
    print()

response_dict = json.loads(data)

weather_temp =  response_dict["list"][0]["main"]["temp"]
humidity =      response_dict["list"][0]["main"]["humidity"]
wind_speed =    response_dict["list"][0]["wind"]["speed"]

feels_like_temp = response_dict["list"][0]["main"]["feels_like"]
feels_like_temp_str = f"{round(int(feels_like_temp))} Fahrenheit"

date =          response_dict["list"][0]["dt_txt"]


weather_data["Today"] = {}

weather_data["Today"]["temperature"] = ""
weather_data["Today"]["humidity"] = ""
weather_data["Today"]["wind_speed"] = ""
weather_data["Today"]["feels_like_temp"] = ""
weather_data["Today"]["date"] = ""

weather_data["Today"]["temperature"] = weather_temp
weather_data["Today"]["humidity"] = humidity
weather_data["Today"]["wind_speed"] = wind_speed
weather_data["Today"]["feels_like_temp"] = feels_like_temp_str
weather_data["Today"]["date"] = date


weather_temp =  response_dict["list"][8]["main"]["temp"]
humidity =      response_dict["list"][8]["main"]["humidity"]
wind_speed =    response_dict["list"][8]["wind"]["speed"]

feels_like_temp = response_dict["list"][8]["main"]["feels_like"]
feels_like_temp_str = f"{round(int(feels_like_temp))} Fahrenheit"

date =          response_dict["list"][8]["dt_txt"]
date_splitted =          date.split(" ")[0]
date_splitted =          date_splitted.split("-")[2]

interval = date.split(" ")[1]
interval = interval.split(":")[0]
interval = int(interval)


weather_data["Tomorrow"] = {}

weather_data["Tomorrow"]["temperature"] = ""
weather_data["Tomorrow"]["humidity"] = ""
weather_data["Tomorrow"]["wind_speed"] = ""
weather_data["Tomorrow"]["feels_like_temp"] = ""
weather_data["Tomorrow"]["date"] = ""

weather_data["Tomorrow"]["temperature"] = weather_temp
weather_data["Tomorrow"]["humidity"] = humidity
weather_data["Tomorrow"]["wind_speed"] = wind_speed
weather_data["Tomorrow"]["feels_like_temp"] = feels_like_temp_str
weather_data["Tomorrow"]["date"] = date

weather_data_to_save = json.dumps(weather_data)

match interval:
    case 3:
        file = "/home/time-traveller/macros/scripts/cdh/weather/weather_new_data_1d_1d_1t.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            f.write(weather_data_to_save)
    
    case 6:
        file = "/home/time-traveller/macros/scripts/cdh/weather/weather_new_data_1d_1d_1t.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            f.write(weather_data_to_save)
    
    case 9:
        file = "/home/time-traveller/macros/scripts/cdh/weather/weather_new_data_1d_1d_2t.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            f.write(weather_data_to_save)
    
    case 12:
        file = "/home/time-traveller/macros/scripts/cdh/weather/weather_new_data_1d_1d_2t.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            f.write(weather_data_to_save)

    case 15:
        file = "/home/time-traveller/macros/scripts/cdh/weather/weather_new_data_1d_1d_3t.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            f.write(weather_data_to_save)
    
    case 18:
        file = "/home/time-traveller/macros/scripts/cdh/weather/weather_new_data_1d_1d_3t.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            f.write(weather_data_to_save)

    case 21:
        file = "/home/time-traveller/macros/scripts/cdh/weather/weather_new_data_1d_1d_4t.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            f.write(weather_data_to_save)
    
    case 0:
        file = "/home/time-traveller/macros/scripts/cdh/weather/weather_new_data_1d_1d_4t.txt"

        with open(file=file, mode="wt", encoding="utf-8") as f:
            f.write(weather_data_to_save)
