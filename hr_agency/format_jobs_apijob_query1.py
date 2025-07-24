import json
from format_unicode import format_stroke


jobs_data = ""
file = "/home/time-traveller/macros/scripts/cdh/raw/hr_agency_apijob_jobs.txt"

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

		job_data = job_data.replace("null", "\"null\"")

		job_data_list = job_data.split("\", \"")

		for value in job_data_list:
			if value.find("\"") >= 0:
				value_filtered = value.split("\"")
				value_filtered = value_filtered[0] + value_filtered[1]

		title = job_data_list[0]
		language = job_data_list[2]
		company = job_data_list[3]
		city = job_data_list[4]
		day = job_data_list[5]
		
		job = [title, language, company, city, day]
		job_filtered = []

		for i in range(2):
			for value in job:
				value_to_filter = value
				index_number = value.find("\"")

				if index_number >= 0:
					value_to_filter = value_to_filter[:index_number] + value_to_filter[index_number+1:]

				job_filtered.append(value_to_filter)

			job = job_filtered
			job_filtered = []


		company_name_to_filter = job[2]
		company_name = ""

		for i in range(len(company_name_to_filter)):
			value = company_name_to_filter[i]

			if i > 0:
				value = value.lower()

			company_name += value

		company = company_name
		job[2] = company


		city_name_to_filter = job[3]
		city_name = ""
	
		if city_name_to_filter != "null":
			city_name = format_stroke(city_name_to_filter)

		city = city_name
		job[3] = city

		jobs_list.append(job)

jobs_data = jobs_list
jobs_data_to_save = json.dumps(jobs_data)

file = "/home/time-traveller/macros/scripts/cdh/formatted/hr_agency_apijob_jobs.txt"

with open(file=file, mode="at", encoding="utf-8") as f:
    f.write(jobs_data_to_save)
    f.write("\n")
