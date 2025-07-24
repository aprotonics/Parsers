import json

file = "/home/time-traveller/macros/scripts/cdh/hr_agency_hr_agencies.txt"

hr_agencies_data = ""

with open(file=file, mode="rt", encoding="utf-8") as f:
    hr_agencies_data = f.read()

hr_agencies_list = hr_agencies_data.splitlines()

print(len(hr_agencies_list))
print()

for value in hr_agencies_list:
	print(value)
	print()
