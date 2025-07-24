import json
from format_unicode import format_stroke


jobs_data = ""

file = "/home/time-traveller/macros/scripts/cdh/formatted/hr_agency_apijob_jobs.txt"


with open(file=file, mode="rt", encoding="utf-8") as f:
    jobs_data = f.readlines()


jobs_data_length = len(jobs_data)
lines_formatted = []

for i in range(1):
    value = jobs_data[i]
    lines = value.split(", [")
    lines_length = len(lines)

    for i in range(lines_length):
        line = lines[i]

        match i:
            case 0:
                line_formatted = line[2:-1]
            case _:
                if i == lines_length-1:
                    line_formatted = line[:-3]
                else:
                    line_formatted = line[:-1]

        line_formatted = line_formatted + "\n"
        lines_formatted.append(line_formatted)
        line_formatted = ""

for i in range(2, jobs_data_length):
    value = jobs_data[i]
    lines = value.split(", [")
    lines_length = len(lines)

    for i in range(lines_length):
        line = lines[i]

        match i:
            case 0:
                line_formatted = line[2:-1]
            case _:
                if i == lines_length-1:
                    line_formatted = line[:-3]
                else:
                    line_formatted = line[:-1]

        line_formatted = line_formatted + "\n"
        lines_formatted.append(line_formatted)
        line_formatted = ""


file = "/home/time-traveller/macros/scripts/cdh/formatted/filtered/hr_agency_apijob_jobs.txt"

with open(file=file, mode="at", encoding="utf-8") as f:
    f.writelines(lines_formatted)
