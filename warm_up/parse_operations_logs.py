import os

file = "/home/time-traveller/macros/scripts/scripts_stage_six/scripts_stage_five/scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/data/operations_logs.txt"

data_to_read = []
result1 = False
result2 = False
result3 = False

with open(file=file, mode="rt", encoding="utf-8") as f:
    data_to_read = f.readlines()


for i in range(len(data_to_read)):
    match data_to_read[i][:-1]:
        case "Warm up has been done":
            result1 = True
        case "HDD has been mounted":
            result2 = True
        case "backup has been done":
            result3 = True


scripts_list1 = os.listdir("/home/time-traveller/macros/scripts/scripts_stage_six/scripts_stage_five/scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/secondary_scripts")
scripts_list2 = os.listdir("/home/time-traveller/macros/scripts/scripts_stage_six/scripts_stage_five/scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one")
scripts_list3 = os.listdir("/home/time-traveller/macros/scripts/scripts_stage_six/scripts_stage_five/scripts_stage_four/scripts_stage_three/scripts_stage_two")
scripts_list4 = os.listdir("/home/time-traveller/macros/scripts/scripts_stage_six/scripts_stage_five/scripts_stage_four/scripts_stage_three")
scripts_list5 = os.listdir("/home/time-traveller/macros/scripts/scripts_stage_six/scripts_stage_five/scripts_stage_four")
scripts_list6 = os.listdir("/home/time-traveller/macros/scripts/scripts_stage_six/scripts_stage_five")
scripts_list7 = os.listdir("/home/time-traveller/macros/scripts/scripts_stage_six")
scripts_list8 = os.listdir("/home/time-traveller/macros/scripts")
scripts_list9 = os.listdir("/home/time-traveller/macros/patches")

scripts_lists = [scripts_list1, scripts_list2, scripts_list3, scripts_list4, scripts_list5, scripts_list6, scripts_list7, scripts_list8, \
                scripts_list9]

scripts_backup_list1 = os.listdir("/media/time-traveller/disk_to_mount/Coding/Scripts/scripts_stage_six/scripts_stage_five/scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/secondary_scripts")
scripts_backup_list2 = os.listdir("/media/time-traveller/disk_to_mount/Coding/Scripts/scripts_stage_six/scripts_stage_five/scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one")
scripts_backup_list3 = os.listdir("/media/time-traveller/disk_to_mount/Coding/Scripts/scripts_stage_six/scripts_stage_five/scripts_stage_four/scripts_stage_three/scripts_stage_two")
scripts_backup_list4 = os.listdir("/media/time-traveller/disk_to_mount/Coding/Scripts/scripts_stage_six/scripts_stage_five/scripts_stage_four/scripts_stage_three")
scripts_backup_list5 = os.listdir("/media/time-traveller/disk_to_mount/Coding/Scripts/scripts_stage_six/scripts_stage_five/scripts_stage_four")
scripts_backup_list6 = os.listdir("/media/time-traveller/disk_to_mount/Coding/Scripts/scripts_stage_six/scripts_stage_five")
scripts_backup_list7 = os.listdir("/media/time-traveller/disk_to_mount/Coding/Scripts/scripts_stage_six")
scripts_backup_list8 = os.listdir("/media/time-traveller/disk_to_mount/Coding/Scripts")
scripts_backup_list9 = os.listdir("/media/time-traveller/disk_to_mount/Coding/Patches")

scripts_backup_lists = [scripts_backup_list1, scripts_backup_list2, scripts_backup_list3, scripts_backup_list4, \
                        scripts_backup_list5, scripts_backup_list6, scripts_backup_list7, scripts_backup_list8, scripts_backup_list9]

for value in scripts_lists:
    value.sort()

for value in scripts_backup_lists:
    value.sort()

backup_result = True
backup_result1 = True
backup_result2 = True
backup_result3 = True
backup_result4 = True
backup_result5 = True
backup_result6 = True
backup_result7 = True
backup_result8 = True
backup_result9 = True

backup_results = [backup_result1, backup_result2, backup_result3, backup_result4, backup_result5, backup_result6, backup_result7, \
                    backup_result8, backup_result9]

for i in range(len(scripts_lists)):
    backup_result = backup_results[i]

    if len(scripts_lists[i]) != len(scripts_backup_lists[i]):
        backup_result = False

for i in range(len(scripts_lists)):
    backup_result = backup_results[i]
    
    scripts_list = scripts_lists[i]
    scripts_backup_list = scripts_backup_lists[i]

    if len(scripts_list) == len(scripts_backup_list):
        scripts_list_dict = {}
        
        for value in scripts_list:
            scripts_list_dict[value] = False

        for i in range(len(scripts_list)):
            for j in range(len(scripts_backup_list)):
                if scripts_list[i] == scripts_backup_list[j]:
                    scripts_list_dict[scripts_list[i]] = True
        
        for value in scripts_list_dict.values():
            if value == False:
                backup_result = False
 
if backup_result1 and backup_result2 and backup_result3 and backup_result4 and backup_result5 and backup_result6 and\
backup_result7 and backup_result8 and backup_result9:
    backup_result = True


for i in range(len(data_to_read)):
    match data_to_read[i][:-1]:
        case "Warm up has not been done":
            result1 = False
        case "Mount is denied because the NTFS volume is already exclusively opened.":
            result2 = False
        case "backup has not been done":
            result3 = False

if backup_result == False:
    result3 = False

if result1 and result2 and result3:
    print("Logs are correct")
else:
    print("Logs are incorrect")
