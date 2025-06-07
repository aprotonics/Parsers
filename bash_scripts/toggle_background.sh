#!/bin/bash

background_images_path="/media/time-traveller/disk_to_mount/Media/Visualities/Images/5/*"

background_image=$(gsettings get org.gnome.desktop.background picture-uri)
background_image2=""
background_image="${background_image##*/}"

count=0

for file in $background_images_path
	do
		((count+=1))
	done


files=()

for file in $background_images_path
	do
		files+=("$file")
	done


for (( i=0 ; i<$count ; i++ ))
	do	
		file="'file:///${files[$i]}'"
		file="${file##*/}"

		if [ "$file" == "$background_image" ]
			then	
				((i++))
				next_file="'file:///${files[$i]}'"
				gsettings set org.gnome.desktop.background picture-uri "$next_file"
				background_image2=$(gsettings get org.gnome.desktop.background picture-uri)
		fi
	done


if [ "$background_image2" == "" ]
	then	
		file="'file:///${files[0]}'"
		gsettings set org.gnome.desktop.background picture-uri "$file"
		background_image2=$(gsettings get org.gnome.desktop.background picture-uri)
fi


background_image2="${background_image2##*/}"


if [ "$background_image" != "$background_image2" ]
	then
		echo ""
		echo "background has been changed"
fi


echo " "
echo " "
echo " "

