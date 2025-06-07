import requests


url = f'https://eodhd.com/api/fundamentals/AAPL.US?api_token=demo&fmt=json'
data = requests.get(url).json()

general_data = data["Highlights"]

print(general_data)
