import requests
import json


jobs_data = []

url = "https://jobs-search-api.p.rapidapi.com/getjobs"

payload = {
	"search_term": "web",
	"location": "boston",
	"results_wanted": 10,
	"site_name": ["indeed", "linkedin", "zip_recruiter", "glassdoor"],
	"distance": 50,
	"job_type": "fulltime",
	"is_remote": False,
	"linkedin_fetch_description": False,
	"hours_old": 48
}

headers = {
	"x-rapidapi-key": "890a769d58msh627a0d6fa7c863dp188549jsn1e2afce6216e",
	"x-rapidapi-host": "jobs-search-api.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

response_dict = json.loads(response.text)

jobs = list()
job_titles = []
companies_titles = []
locations = []

for value in response_dict["jobs"]:
	job_title = value["title"]
	company_title = value["company"]
	location = value["location"]

	job_titles.append(job_title)
	companies_titles.append(company_title)
	locations.append(location)
	
	job = [job_title, company_title, location]
	jobs.append(job)

jobs_data = jobs
jobs_data_to_save = json.dumps(jobs_data)


file = "/home/time-traveller/macros/scripts/cdh/hr/raw/hr_agency_jobs_search_jobs.txt"

with open(file=file, mode="at", encoding="utf-8") as f:
    f.write(jobs_data_to_save)
    f.write("\n")
