#!/bin/bash

Monitorslog1=$(xrandr --listmonitors | grep "*")
Monitorslog1="${Monitorslog1##* }"
MONITOR="$Monitorslog1"
xrandr --output "$MONITOR" --gamma 1.4:1.4:1.4

echo " "
echo " "


