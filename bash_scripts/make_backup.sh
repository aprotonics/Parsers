#!/bin/bash

for file in /media/time-traveller/disk_to_mount/Coding/Scripts/*
	do
		rm -r $file
	done

for file in /media/time-traveller/disk_to_mount/Coding/Patches/*
	do
		rm -r $file
	done


for file in /home/time-traveller/macros/scripts/*
	do
		if [ "$file" != "/home/time-traveller/macros/scripts/scripts_stage_four/scripts_stage_three/scripts_stage_two/scripts_stage_one/make_backup.sh" ]
			then
				cp -r $file /media/time-traveller/disk_to_mount/Coding/Scripts
				echo "file $file has been copied"
		fi
	done

for file in /home/time-traveller/macros/patches/*
	do
		cp -r $file /media/time-traveller/disk_to_mount/Coding/Patches
		echo "file $file has been copied"
	done


echo " "
echo "backup has been done"
echo " "
echo " "
echo " "

