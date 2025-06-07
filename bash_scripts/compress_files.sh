#!/bin/bash

file="update_copy.sh"

gzip -k -c "$file" > "/home/time-traveller/Downloads/$file.gz"
tar -czf "/home/time-traveller/Downloads/$file.tar.gz" "$file"

echo "file $file has been compressed"
echo " "
echo " "


