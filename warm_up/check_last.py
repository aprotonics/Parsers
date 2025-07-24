import os
from main.check_last_value import is_last_simple


file = "/home/time-traveller/macros/scripts/scripts_stage_six/"\
    "scripts_stage_five/scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/data/warm_up_data/warm_up.txt"


with open(file=file, mode="rt", encoding="utf-8") as f:

    array = f.readlines()


last_stroke = array[len(array)-2].rstrip()
last_stroke = last_stroke.split(", ")
is_simple, last = is_last_simple(last_stroke)
is_last_new = False

if is_simple:

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
        if len(value.split("backup")[1].split(".")[0]):
            warm_up_backups_list.append(int(value.split("backup")[1].split(".")[0]))

    max_value = 0

    for value in warm_up_backups_list:
        if value > max_value:
            max_value = value

    previous_backup = max_value


    file = f"/home/time-traveller/macros/scripts/scripts_stage_six/scripts_stage_five/"\
        f"scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/data/warm_up_data/warm_up_backup{previous_backup}.txt"

    with open(file=file, mode="rt", encoding="utf-8") as f:

        array = f.readlines()


    previous_stroke = array[len(array)-2].rstrip()
    previous_stroke = previous_stroke.split(", ")
    is_previous_simple, previous = is_last_simple(previous_stroke)

    if last > previous:
        is_last_new = True


if is_last_new:
    print("Warm up done")
else:
    print("Warm up has not been done")
