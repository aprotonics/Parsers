import requests


EXCHANGE_CODE = "BA"

url = f'https://eodhd.com/api/exchange-symbol-list/{EXCHANGE_CODE}?api_token=6707e3317287a8.60947566&fmt=json'

data = requests.get(url).json()

inc_data = ""

for value in data:
    if value["Code"] == "AAPL":
        inc_data = value
        print(inc_data)
