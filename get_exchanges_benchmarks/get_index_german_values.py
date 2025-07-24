import json


file = "/home/time-traveller/macros/scripts/cdh/global_indexes/global_index_data_dax40_filtered.txt"

inc_data_json = ""

with open(file=file, mode="rt", encoding="utf-8") as f:
    inc_data_json = f.read()

inc_data_lines = inc_data_json.splitlines()
inc_data_lines_length = len(inc_data_lines)
inc_yesterday_data = inc_data_lines[inc_data_lines_length-1]

inc_yesterday_data = inc_yesterday_data[1:-1]
inc_yesterday_data = inc_yesterday_data.split(", ")[0]
inc_yesterday_data = inc_yesterday_data.split(": ")[1]
inc_yesterday_data = inc_yesterday_data[1:-1]
inc_yesterday_data = inc_yesterday_data.split("-")[1]
index_daily_data_confirmed = []

for i in range(inc_data_lines_length):
    index_daily_data = inc_data_lines[i]
    index_daily_data = index_daily_data[1:-1]
    index_daily_data_filtered = index_daily_data.split(", ")[0].split(": ")[1][1:-1].split("-")[1]

    if index_daily_data_filtered == "12":
        index_daily_data_confirmed.append(index_daily_data)

    if index_daily_data_filtered == "01":
        index_daily_data_confirmed.append(index_daily_data)

index_month_data_filtered = []

for value in index_daily_data_confirmed:

    index_month_data = value

    index_month_data_day_filtered_dict = []
    index_month_data_close_filtered_dict = []

    index_month_data_day_filtered = index_month_data.split(", ")[0].split(": ")[1][1:-1]
    index_month_data_day_filtered_dict.append(index_month_data_day_filtered)

    index_month_data_close_filtered = index_month_data.split(", ")[4].split(": ")[1]
    index_month_data_close_filtered_dict.append(index_month_data_close_filtered)

    index_month_data_filtered.append(index_month_data_day_filtered_dict)
    index_month_data_filtered.append(index_month_data_close_filtered_dict)


print(index_month_data_filtered)
print()
