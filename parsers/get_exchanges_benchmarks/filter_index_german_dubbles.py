
file = "/home/time-traveller/macros/scripts/cdh/global_indexes/global_index_data_dax40.txt"

inc_data = ""

with open(file=file, mode="rt", encoding="utf-8") as f:
    inc_data = f.read()

inc_data_json = ""

with open(file=file, mode="rt", encoding="utf-8") as f:
    inc_data_json = f.read()

inc_data_lines = inc_data_json.splitlines()
inc_data_lines_length = len(inc_data_lines)

inc_data = []

for i in range(inc_data_lines_length):
    is_to_filtered = False

    value = inc_data_lines[i]
    value_day = value.split("\", \"")[0].split(": \"")[1]

    for k in range(i + 1, inc_data_lines_length):
        if value_day == inc_data_lines[k].split("\", \"")[0].split(": \"")[1]:
            is_to_filtered = True
    
    if not is_to_filtered:    
        inc_data.append(value)


file = "/home/time-traveller/macros/scripts/cdh/global_indexes/global_index_data_dax40_filtered.txt"

inc_data_lines = []

for value in inc_data:
    value += "\n"
    inc_data_lines.append(value)

inc_data = inc_data_lines

with open(file=file, mode="wt", encoding="utf-8") as f:
    f.writelines(inc_data)
