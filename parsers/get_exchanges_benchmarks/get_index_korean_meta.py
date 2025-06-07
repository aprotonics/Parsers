import json
from os import error
import time


day_now = int(time.ctime(time.time()).split(" ")[2].split(":")[0])
time_now = int(time.ctime(time.time()).split(" ")[3].split(":")[0])

try:

    file = "/home/time-traveller/macros/scripts/cdh/global_indexes/global_index_data_krx100.txt"
    inc_data_json = ""

    with open(file=file, mode="rt", encoding="utf-8") as f:
        inc_data_json = f.read()

    inc_data_lines = inc_data_json.splitlines()
    inc_data_lines_length = len(inc_data_lines)
    inc_yesterday_data = inc_data_lines[inc_data_lines_length-1]
    inc_yesterday = inc_yesterday_data.split("{")[1].split("}")[0].split(", ")[0].split("\"")[3].split("-")[2]

    if int(day_now) - 1 == int(inc_yesterday):
        print("Korean benchmark is up to date")
    else:
        print("Korean benchmark is deprecated")
        print(f"Korean benchmark is by date {inc_yesterday}")

except OSError:
    print("There is no file with that name")
