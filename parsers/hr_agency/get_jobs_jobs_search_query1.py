import json

jobs_data = ""
file = "/home/time-traveller/macros/scripts/cdh/hr/raw/hr_agency_jobs_search_jobs.txt"

with open(file=file, mode="rt", encoding="utf-8") as f:
    jobs_data = f.read()

jobs_data_lists = jobs_data.splitlines()

jobs_list = []
jobs_amount = 0

for i in range(len(jobs_data_lists)):
	jobs_data_list = jobs_data_lists[i]
	jobs_data_list = jobs_data_list[1:len(jobs_data_list)-1]
	
	jobs_data = jobs_data_list.split("], [")

	jobs_amount += len(jobs_data)

	if i == len(jobs_data_lists) - 1:
		length_of_last_jobs_data_list = len(jobs_data)

	for i in range(len(jobs_data)):
		job_data = jobs_data[i]

		if i == 0:
			job_data = job_data[1:]

		if i == len(jobs_data) - 1:
			job_data = job_data[:len(job_data)-1]

		job_data_list = job_data.split("\", \"")

		job_title = job_data_list[0]
		company_title = job_data_list[1]
		location = job_data_list[2]
		
		job = [job_title, company_title, location]
		job_filtered = []

		for value in job:
			value_to_filter = value
			index_number = value.find("\"")

			if index_number >= 0:
				value_to_filter = value_to_filter[:index_number] + value_to_filter[index_number+1:]

			job_filtered.append(value_to_filter)

		job = job_filtered
		job_filtered = []

		jobs_list.append(job)

for i in range(jobs_amount - length_of_last_jobs_data_list, len(jobs_list)):
	print(jobs_list[i])
