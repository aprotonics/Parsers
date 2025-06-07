import requests


url = f'https://eodhd.com/api/exchanges-list/?api_token=6707e3317287a8.60947566&fmt=json'

data = requests.get(url).json()

for value in data:
    print(value)
