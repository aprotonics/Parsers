#!/bin/bash

urls=("ox.ac.uk" "google.com")

for url in "${urls[@]}"
	do
		ping -c 2 $url
		echo " "
		echo " "
	done

