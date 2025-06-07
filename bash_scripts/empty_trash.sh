#!/bin/bash


for file in /home/time-traveller/.local/share/Trash/files/*
	do
		rm "$file"
		rm -r "$file"
		echo "file/folder $file has been deleted"	
	done

for file in /media/time-traveller/8EF6D665F6D64D59/.Trash-1000/files/*
	do
		rm "$file"
		rm -r "$file"
	done

for file in /media/time-traveller/A418A1E418A1B5A8/.Trash-1000/files/*
	do
		rm "$file"
		rm -r "$file"
	done

echo " "
echo " "

