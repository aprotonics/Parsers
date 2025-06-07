#!/bin/bash

while read line
	do
	
		sudo apt install "$line"
		echo " "
		
	done < "packages.txt"

echo " "
echo " "

