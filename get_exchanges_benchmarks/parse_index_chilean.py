import requests
import json


inc_token = "DBXD.SN"
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


file = "/home/time-traveller/macros/scripts/cdh/global_indexes/global_index_data_igpa50.txt"

with open(file=file, mode="at", encoding="utf-8") as f:
    f.write(inc_data_to_save)
    f.write("\n")
