import requests


EXCHANGE_CODE = "US"

url = f'https://eodhd.com/api/exchange-symbol-list/{EXCHANGE_CODE}?api_token=6707e3317287a8.60947566&fmt=json'

data = requests.get(url).json()

print(len(data))


inc_data = ""

for value in data:
    if value["Code"] == "AAPL":
        inc_data = value
        print(inc_data)


incs_exchange_list = data
inc_data_to_save = incs_exchange_list

file = "/home/time-traveller/macros/scripts/cdh/global_indexes/list_of_incs_exchange.txt"

with open(file=file, mode="wt", encoding="utf-8") as f:

    for value in incs_exchange_list:
        value = str(value)
        f.write(value)
        f.write("\n")
