import requests
import json


jobs_data = {}

url = "https://jobs-api14.p.rapidapi.com/v2/list"

querystring = {"query": "Frontend Developer", "location": "United States"}

headers = {
	"x-rapidapi-key": "890a769d58msh627a0d6fa7c863dp188549jsn1e2afce6216e",
	"x-rapidapi-host": "jobs-api14.p.rapidapi.com"
}

response = "response text"

response_dict = json.loads(response)

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

for i in range(len(jobs)):
	jobs_data[f"job{i+1}"] = jobs[i]

jobs_data_to_save = json.dumps(jobs_data)


file = "/home/time-traveller/macros/scripts/cdh/hr_agency_jobs.txt"

with open(file=file, mode="at", encoding="utf-8") as f:
    f.write(jobs_data_to_save)
    f.write("\n")
