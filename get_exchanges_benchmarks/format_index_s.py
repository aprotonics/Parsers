import json


file = "/home/time-traveller/macros/scripts/cdh/global_indexes/global_index_data_sp500.txt"
inc_data = ""

with open(file=file, mode="rt", encoding="utf-8") as f:
    inc_data = f.read()


inc_data_lines = inc_data.splitlines()
inc_data_lines_length = len(inc_data_lines)

inc_lines = []
inc_line_formatted = ""
inc_line_values = []
inc_data = []

for i in range(len(inc_data_lines)):
    value = inc_data_lines[i]
    inc_line = value[1:-1]
    inc_line_list = inc_line.split(", ")
    inc_line_list_length = len(inc_line_list)

    for j in range(inc_line_list_length):
        value = inc_line_list[j]

        if j >= 1 and j <= inc_line_list_length-2:
            inc_line = inc_line_list[j].split(": ")
            inc_line_value = inc_line[1]

            if len(inc_line_value) == 6:
                inc_line_value
                inc_line_value_list = inc_line_value.split(".")
                inc_line_value = int(inc_line_value_list[0]) + int(inc_line_value_list[1]) / 100
                inc_line_value = round(inc_line_value, 1)

            inc_line_values.append(inc_line_value)
    
    stroke1 = "date"
    stroke2 = "open"
    stroke3 = "high"
    stroke4 = "low"
    stroke5 = "close"
    stroke6 = "adjusted_close"
    stroke7 = "volume"

    inc_line_date = inc_line_list[0]
    inc_line_volume = inc_line_list[len(inc_line_list)-1]
    inc_line_date_value = inc_line_date.split(": ")[1]
    inc_line_date_value = inc_line_date_value[1:-1]
    inc_line_volume_value = inc_line_volume.split(": ")[1]

    inc_lines_dict = {}

    inc_lines_dict[stroke1] = inc_line_date_value
    inc_lines_dict[stroke2] = inc_line_values[0]
    inc_lines_dict[stroke3] = inc_line_values[1]
    inc_lines_dict[stroke4] = inc_line_values[2]
    inc_lines_dict[stroke5] = inc_line_values[3]
    inc_lines_dict[stroke6] = inc_line_values[4]
    inc_lines_dict[stroke7] = inc_line_volume_value

    inc_data.append(inc_lines_dict)

    inc_line_values = []

value_formatted = json.dumps(inc_data[0])
values_formatted = []

for i in range(len(inc_data)):
    value_formatted = json.dumps(inc_data[i])
    values_formatted.append(value_formatted)


file = "/home/time-traveller/macros/scripts/cdh/global_indexes/formatted/global_index_data_sp500_formatted.txt"
inc_data_lines = []

for value in values_formatted:
    value_formatted = value[1:-1] + "\n"
    inc_data_lines.append(value_formatted)

inc_data = inc_data_lines

with open(file=file, mode="wt", encoding="utf-8") as f:
    f.writelines(inc_data)
