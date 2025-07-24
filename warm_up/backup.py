import os
from main.clasterize import clasterize_array


file = "/home/time-traveller/macros/scripts/scripts_stage_six/"\
    "scripts_stage_five/scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/data/warm_up_data/warm_up.txt"

with open(file=file, mode="rt", encoding="utf-8") as f:

        array = f.readlines()


numbers_array_clasterized = clasterize_array(array)


file = "/home/time-traveller/macros/scripts/scripts_stage_six/scripts_stage_five/"\
    "scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/data/warm_up_data/warm_up_backup_candidate.txt"

with open(file=file, mode="wt", encoding="utf-8") as f:

    for numbers_array_clasterized_value in numbers_array_clasterized:
        for value in numbers_array_clasterized_value:
            value = str(value)
            value = value[:-1]
            value += "\n"

            f.write(value)

    f.write("\n")


backup_candidate = file

previous_backup = int()
warm_up_directory_list = []
warm_up_backup_directory_list = []
warm_up_backups_list = []

warm_up_directory_list = os.listdir("/home/time-traveller/macros/scripts/scripts_stage_six/"\
    "scripts_stage_five/scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/data/warm_up_data")

for value in warm_up_directory_list:
    if len(value.split("backup")) > 1:
        warm_up_backup_directory_list.append(value)

warm_up_backup_directory_list.sort()

for value in warm_up_backup_directory_list:
    if value.split("backup")[1].split(".")[0][:1].isnumeric():
        if len(value.split("backup")[1].split(".")[0]):
            warm_up_backups_list.append(int(value.split("backup")[1].split(".")[0]))

    max_value = 0

for value in warm_up_backups_list:
    if value > max_value:
        max_value = value

previous_backup = max_value
next_backup = previous_backup + 1

file = f"/home/time-traveller/macros/scripts/scripts_stage_six/scripts_stage_five/"\
    f"scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/data/warm_up_data/warm_up_backup{next_backup}.txt"

os.rename(backup_candidate, file)
