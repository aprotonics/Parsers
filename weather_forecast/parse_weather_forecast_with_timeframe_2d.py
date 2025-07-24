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


for i in range(8, 24, 8):
    weather_temp =  response_dict["list"][i]["main"]["temp"]
    humidity =      response_dict["list"][i]["main"]["humidity"]
    wind_speed =    response_dict["list"][i]["wind"]["speed"]

    feels_like_temp = response_dict["list"][i]["main"]["feels_like"]
    feels_like_temp_str = f"{round(int(feels_like_temp))} Fahrenheit"

    date =          response_dict["list"][i]["dt_txt"]
    date_splitted =          date.split(" ")[0]
    date_splitted =          date_splitted.split("-")[2]

    interval = date.split(" ")[1]
    interval = interval.split(":")[0]
    interval = int(interval)


    phrodo_phroneme = ""


    if int(date_splitted) == 1 or int(date_splitted) == 21:

        phrodo_phroneme = "st"

        weather_data[f"{date_splitted}{phrodo_phroneme} day"] = {}

        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["temperature"] = ""
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["humidity"] = ""
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["wind_speed"] = ""
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["feels_like_temp"] = ""
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["date"] = ""

        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["temperature"] = weather_temp
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["humidity"] = humidity
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["wind_speed"] = wind_speed
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["feels_like_temp"] = feels_like_temp_str
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["date"] = date

    if int(date_splitted) == 2 or int(date_splitted) == 22:
        
        phrodo_phroneme = "nd"

        weather_data[f"{date_splitted}{phrodo_phroneme} day"] = {}

        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["temperature"] = ""
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["humidity"] = ""
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["wind_speed"] = ""
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["feels_like_temp"] = ""
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["date"] = ""

        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["temperature"] = weather_temp
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["humidity"] = humidity
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["wind_speed"] = wind_speed
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["feels_like_temp"] = feels_like_temp_str
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["date"] = date

    if int(date_splitted) == 3 or int(date_splitted[1:]) == 23:
        
        phrodo_phroneme = "rd"

        weather_data[f"{date_splitted}{phrodo_phroneme} day"] = {}

        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["temperature"] = ""
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["humidity"] = ""
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["wind_speed"] = ""
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["feels_like_temp"] = ""
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["date"] = ""

        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["temperature"] = weather_temp
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["humidity"] = humidity
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["wind_speed"] = wind_speed
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["feels_like_temp"] = feels_like_temp_str
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["date"] = date

    if 3 < int(date_splitted) <= 20 or 23 < int(date_splitted) <= 30:

        phrodo_phroneme = "th"

        weather_data[f"{date_splitted}{phrodo_phroneme} day"] = {}

        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["temperature"] = ""
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["humidity"] = ""
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["wind_speed"] = ""
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["feels_like_temp"] = ""
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["date"] = ""

        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["temperature"] = weather_temp
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["humidity"] = humidity
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["wind_speed"] = wind_speed
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["feels_like_temp"] = feels_like_temp_str
        weather_data[f"{date_splitted}{phrodo_phroneme} day"]["date"] = date

    weather_data_to_save = json.dumps(weather_data) 

    day = i // 8

    match interval:
        case 3:
            file = f"/home/time-traveller/macros/scripts/cdh/weather/weather_new_data_2d_{day}d_1t.txt"

            with open(file=file, mode="wt", encoding="utf-8") as f:
                f.write(weather_data_to_save)
    
        case 6:
            file = f"/home/time-traveller/macros/scripts/cdh/weather/weather_new_data_2d_{day}d_1t.txt"

            with open(file=file, mode="wt", encoding="utf-8") as f:
                f.write(weather_data_to_save)
    
        case 9:
            file = f"/home/time-traveller/macros/scripts/cdh/weather/weather_new_data_2d_{day}d_2t.txt"

            with open(file=file, mode="wt", encoding="utf-8") as f:
                f.write(weather_data_to_save)
    
        case 12:
            file = f"/home/time-traveller/macros/scripts/cdh/weather/weather_new_data_2d_{day}d_2t.txt"

            with open(file=file, mode="wt", encoding="utf-8") as f:
                f.write(weather_data_to_save)

        case 15:
            file = f"/home/time-traveller/macros/scripts/cdh/weather/weather_new_data_2d_{day}d_3t.txt"

            with open(file=file, mode="wt", encoding="utf-8") as f:
                f.write(weather_data_to_save)
    
        case 18:
            file = f"/home/time-traveller/macros/scripts/cdh/weather/weather_new_data_2d_{day}d_3t.txt"

            with open(file=file, mode="wt", encoding="utf-8") as f:
                f.write(weather_data_to_save)

        case 21:
            file = f"/home/time-traveller/macros/scripts/cdh/weather/weather_new_data_2d_{day}d_4t.txt"

            with open(file=file, mode="wt", encoding="utf-8") as f:
                f.write(weather_data_to_save)
    
        case 0:
            file = f"/home/time-traveller/macros/scripts/cdh/weather/weather_new_data_2d_{day}d_4t.txt"

            with open(file=file, mode="wt", encoding="utf-8") as f:
                f.write(weather_data_to_save)
