import json


file = "/home/time-traveller/macros/scripts/cdh/sol_hs.txt"

sol_data_json = ""

with open(file=file, mode="rt", encoding="utf-8") as f:
    sol_data_json = f.read()


sol_data = json.loads(sol_data_json)

sol_data_sunrise = sol_data["sunrise"]
sol_data_sunset = sol_data["sunset"]

print("Today's sol data")
print(f"Sunrise on {sol_data_sunrise}")
print(f"Sunset on {sol_data_sunset}")
