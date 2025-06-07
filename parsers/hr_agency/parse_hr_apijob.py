import requests
import json


url = "https://apijob-job-searching-api.p.rapidapi.com/v1/organization/search"

payload = { "q": "Amazon" }
headers = {
	"x-rapidapi-key": "890a769d58msh627a0d6fa7c863dp188549jsn1e2afce6216e",
	"x-rapidapi-host": "apijob-job-searching-api.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(type(response))
print(response)
print(type(response.text))
print()

response_dict = json.loads(response.text)

print(len(response_dict["hits"]))
print()

results = []

for value in response_dict["hits"]:
	results.append(value)
	print(value)

print()
print()

companies = list()

companies_titles = []
companies_url = []

for value in response_dict["hits"]:
	company_title = value["name"]
	company_url = value["domain"]

	companies_titles.append(company_title)
	companies_url.append(company_url)
	
	company = [company_title, company_url]
	companies.append(company)

for value in companies:
	print(value)
