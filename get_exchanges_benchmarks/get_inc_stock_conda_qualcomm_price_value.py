import json


file = "/home/time-traveller/macros/scripts/cdh/global_inc_conda_qualcomm.txt"

inc_data_json = ""

with open(file=file, mode="rt", encoding="utf-8") as f:
    inc_data_json = f.read()

inc_data_lines = inc_data_json.splitlines()
inc_data_lines_length = len(inc_data_lines)
inc_yesterday_data = inc_data_lines[inc_data_lines_length-1]

print(inc_yesterday_data)
print()
