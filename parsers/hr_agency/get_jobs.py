import json

file = "/home/time-traveller/macros/scripts/cdh/hr_agency_jobs.txt"
jobs_data = ""

with open(file=file, mode="rt", encoding="utf-8") as f:
    jobs_data = f.read()

jobs_data_list = jobs_data.splitlines()

print(len(jobs_data_list))
print()

jobs_list = []
jobs = {}
titles = []
companies = []

for i in range(len(jobs_data_list)):
	jobs_data = jobs_data_list[i].split(", \"job")

	results = []

	for i in range(len(jobs_data)):
		value = jobs_data[i]
		str_index = value.find("\": ")
		result_value = value[str_index+3:]

		if i == len(jobs_data) - 1:
			result_value = result_value[:len(result_value)-1]

		results.append(result_value)

	for value in results:
		value = value[1:len(value)-1]

		first_split_index = value.find(", ")
		second_split_index = value.find(", ", first_split_index + 1)

		title = value[:first_split_index]
		company = value[first_split_index+3:second_split_index-1]
		hr_agencies = value[second_split_index+2:]

		titles.append(title)
		companies.append(company)

jobs["titles"] = titles
jobs["companies"] = companies

print(jobs["titles"])
print()

print(jobs["companies"])
print()
