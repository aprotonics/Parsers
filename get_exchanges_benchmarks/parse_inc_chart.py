import requests
import json


inc_token = "AAPL.US"
API_key = "6707e3317287a8.60947566"
url = f"https://eodhd.com/api/eod/{inc_token}"

response = requests.request(
    method="GET",
    url=url,
    params={
        "api_token": API_key,
        "fmt": "json",
    }
)

response_dict = json.loads(response.text)

response_dict_length = len(response_dict)
yesterday_volume = response_dict[response_dict_length-1]

inc_data = yesterday_volume
inc_data_to_save = json.dumps(inc_data)

file = "/home/time-traveller/macros/scripts/cdh/global_inc_data.txt"
inc_data_json = ""

with open(file=file, mode="rt", encoding="utf-8") as f:
    inc_data_json = f.read()

inc_data_lines = inc_data_json.splitlines()
inc_data_lines_length = len(inc_data_lines)
inc_yesterday_data = inc_data_lines[inc_data_lines_length-1]

if inc_data_to_save != inc_yesterday_data:
    with open(file=file, mode="at", encoding="utf-8") as f:
        f.write(inc_data_to_save)
        f.write("\n")
