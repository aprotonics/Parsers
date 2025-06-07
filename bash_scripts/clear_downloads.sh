#!/bin/bash

for file in /home/time-traveller/Downloads/*
	do
		if [ "$file" != "/home/time-traveller/Downloads/tor-browser-linux" ]
			then	
				rm "$file"
				rm -r "$file"
				echo "file $file has been deleted"
		fi
	done

echo " "
echo " "


