import os
import random


path_to_files = "/media/time-traveller/disk_to_mount/Media/Visualities/Images/3"

files_list = os.listdir(path_to_files)

titles = []
title = ""
titles.append(title)
title_changed = False

for value in files_list:
    file_name_to_change = path_to_files + "/" + value
    title_changed = False

    while not title_changed:

        title = str(random.randint(100000, 999999)) + ".jpg"

        if title not in titles:
            file_name_to_change_to = path_to_files + "/" + title
            os.rename(file_name_to_change, file_name_to_change_to)

            titles.append(title)
            title_changed = True
