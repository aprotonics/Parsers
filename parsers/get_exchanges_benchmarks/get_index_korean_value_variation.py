import json


file = "/home/time-traveller/macros/scripts/cdh/global_indexes/global_index_data_krx100_filtered.txt"

inc_data_json = ""

with open(file=file, mode="rt", encoding="utf-8") as f:
    inc_data_json = f.read()

inc_data_lines = inc_data_json.splitlines()
inc_data_lines_length = len(inc_data_lines)

inc_previous_data = inc_data_lines[inc_data_lines_length-1]
inc_previous_data_length = len(inc_previous_data)
inc_previous_data = inc_previous_data[1:inc_previous_data_length-1]
inc_previous_data_list = inc_previous_data.split(", ")
inc_previous_data_close = inc_previous_data_list[4]
inc_previous_data_close_list = inc_previous_data_close.split(": ")

inc_previous_data2 = inc_data_lines[inc_data_lines_length-2]
inc_previous_data2_length = len(inc_previous_data2)
inc_previous_data2 = inc_previous_data2[1:inc_previous_data2_length-1]
inc_previous_data2_list = inc_previous_data2.split(", ")
inc_previous_data2_close = inc_previous_data2_list[4]
inc_previous_data2_close_list = inc_previous_data2_close.split(": ")

inc_previous_data3 = inc_data_lines[inc_data_lines_length-3]
inc_previous_data3_length = len(inc_previous_data3)
inc_previous_data3 = inc_previous_data3[1:inc_previous_data3_length-1]
inc_previous_data3_list = inc_previous_data3.split(", ")
inc_previous_data3_close = inc_previous_data3_list[4]
inc_previous_data3_close_list = inc_previous_data3_close.split(": ")

inc_previous_price = int(inc_previous_data_close_list[1])
inc_previous_price2 = int(inc_previous_data2_close_list[1])
inc_previous_price3 = int(inc_previous_data3_close_list[1])

procentile = int()
procentile = ((inc_previous_price - inc_previous_price2) / inc_previous_price2) * 1000
procentile = round(procentile)


print(str(procentile) + "‰")
