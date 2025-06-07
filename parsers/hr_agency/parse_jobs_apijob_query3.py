import requests
import json


jobs_data = []

url = "https://apijob-job-searching-api.p.rapidapi.com/v1/job/search"

payload = { "q": "agent" }

headers = {
	"x-rapidapi-key": "890a769d58msh627a0d6fa7c863dp188549jsn1e2afce6216e",
	"x-rapidapi-host": "apijob-job-searching-api.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

response_dict = json.loads(response.text)

jobs = list()
job_titles = []
companies_titles = []
vacancies_urls = []
locations = []
languages = []
days = []

for job_response in response_dict["hits"]:
	job_title = None
	vacancy_url = None
	language = None
	company_title = None
	location = None
	day = None

	for key in job_response.keys():
		if key == "title":
			job_title = job_response[key]
		if key == "url":
			vacancy_url = job_response[key]
		if key == "language":
			language = job_response[key]
		if key == "hiringOrganizationName":
			company_title = job_response[key]
		if key == "city":
			location = job_response[key]
		if key == "created_at":
			day = job_response[key]

	job_titles.append(job_title)
	vacancies_urls.append(vacancy_url)
	languages.append(language)
	companies_titles.append(company_title)
	locations.append(location)
	days.append(day)

	job = [job_title, vacancy_url, language, company_title, location, day]
	jobs.append(job)

for i in range(len(response_dict["hits"])):
	job = jobs[i]

jobs_data = jobs

jobs_data_to_save = json.dumps(jobs_data)


file = "/home/time-traveller/macros/scripts/cdh/raw/hr_agency_apijob_jobs_3.txt"

with open(file=file, mode="at", encoding="utf-8") as f:
    f.write(jobs_data_to_save)
    f.write("\n")
