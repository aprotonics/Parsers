import requests
import json


hr_agencies_data = {}

url = "https://jobs-api14.p.rapidapi.com/v2/list"

querystring = {"query": "Games", "location": "United States"}

headers = {
	"x-rapidapi-key": "890a769d58msh627a0d6fa7c863dp188549jsn1e2afce6216e",
	"x-rapidapi-host": "jobs-api14.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

response_dict = json.loads(response.text)

print(response_dict)

jobs = list()

job_titles = []
companies_titles = []
hr_agencies_titles = []

for value in response_dict["jobs"]:
	job_title = value["title"]
	company_title = value["company"]
	hr_agency_title = value["jobProviders"]

	job_titles.append(job_title)
	companies_titles.append(company_title)
	hr_agencies_titles.append(hr_agency_title)
	
	job = [job_title, company_title, hr_agency_title]
	jobs.append(job)

hr_agencies = set()

for hr_agency_titles in hr_agencies_titles:
	for value in hr_agency_titles:
		hr_agency_title = value["jobProvider"]
		hr_agencies.add(hr_agency_title)


hr_agencies_data = list(hr_agencies)
hr_agencies_data_to_save = json.dumps(hr_agencies_data)


file = "/home/time-traveller/macros/scripts/cdh/hr_agency_hr_agencies.txt"

with open(file=file, mode="at", encoding="utf-8") as f:
    f.write(hr_agencies_data_to_save)
    f.write("\n")
