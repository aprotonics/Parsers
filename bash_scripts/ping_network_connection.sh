#!/bin/bash

urls=("ox.ac.uk" "google.com" "youtube.com" "cam.ac.uk" "harvard.edu" "stanford.edu" "portal.uab.pt" "mercadolibre.com.ar" "asus.com" "lmu.de" "uni-muenster.de" "museodelprado.es")

for url in "${urls[@]}"
	do
		ping -c 4 $url
		echo " "
		echo " "
	done




