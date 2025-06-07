#!/bin/bash

file="tsetup.5.6.1.tar.gz"


gzip -dk "$file"
tar -xf "$file" -C /home/time-traveller/Downloads

echo "file $file has been extracted"
echo " "
echo " "


