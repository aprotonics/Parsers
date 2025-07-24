import requests
import json
import time


inc_token = "AMD.US"
API_key = "6707e3317287a8.60947566"
url = f"https://eodhd.com/api/eod/{inc_token}"

def fetch_with_time_out(url, API_key, timeout):
    url = url
    API_key = API_key
    timeout = timeout

    start = time.time()
    data = ""

    with requests.get(url, params={"api_token": API_key, "fmt": "json"}, stream=True) as response:
        response.raise_for_status()

        data = bytearray()

        for chunk in response.iter_content(chunk_size=8192):
            if time.time() - start > timeout:
                raise TimeoutError()

            data.extend(chunk)

    return data

try:
    data = fetch_with_time_out(url, API_key, 5)
except TimeoutError as err:
    print()
    print()
    print(err)
    print("Time of requesting has exceeded timeout limit")
    print()

response_dict = json.loads(data)


response_dict_length = len(response_dict)
yesterday_volume = response_dict[response_dict_length-1]

inc_data = yesterday_volume
inc_data_to_save = json.dumps(inc_data)

file = "/home/time-traveller/macros/scripts/cdh/global_inc_conda_amd.txt"
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
