import requests


EXCHANGE_CODE = "VI"

url = f'https://eodhd.com/api/exchange-symbol-list/{EXCHANGE_CODE}?api_token=6707e3317287a8.60947566&fmt=json'

data = requests.get(url).json()

inc_data = ""

print(data)
print()
print(len(data))

for value in data:
    if value["Code"] == "GAGS":
        inc_data = value
        print(inc_data)
