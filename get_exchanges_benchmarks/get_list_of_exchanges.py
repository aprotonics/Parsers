import requests


url = f'https://eodhd.com/api/exchanges-list/?api_token=6707e3317287a8.60947566&fmt=json'

data = requests.get(url).json()

for value in data:
    print(value)


exchanges_data_to_save = data

file = "/home/time-traveller/macros/scripts/cdh/global_indexes/list_of_exchanges.txt"

with open(file=file, mode="wt", encoding="utf-8") as f:

    for value in exchanges_data_to_save:
        value = str(value)
        f.write(value)
        f.write("\n")
