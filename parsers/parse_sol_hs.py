import requests
import json


url = "https://api.sunrise-sunset.org/json"
latitude = "56.7927462"
longitude = "60.1454412"
timezone_id = "Asia/Yekaterinburg"

response = requests.request(
    method="GET",
    url=url,
    params={
        "lat": latitude,
        "lng": longitude,
        "tzid": timezone_id
    }
)

response_dict = json.loads(response.text)

sunrise = response_dict["results"]["sunrise"]
sunset = response_dict["results"]["sunset"]

sol_data = {}

sol_data["sunrise"] = ""
sol_data["sunset"] = ""

sol_data["sunrise"] = sunrise
sol_data["sunset"] = sunset


data_to_save = json.dumps(sol_data)


file = "/home/time-traveller/macros/scripts/cdh/sol_hs.txt"

with open(file=file, mode="wt", encoding="utf-8") as f:
    f.write(data_to_save)
