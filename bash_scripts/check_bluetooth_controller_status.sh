#!/bin/bash

bluetoothctl_log1=$(bluetoothctl show | grep "Powered:")
bluetoothctl_log2=$(bluetoothctl show | grep "Discoverable:")
bluetoothctl_log3=$(bluetoothctl show | grep "Pairable:")

echo "$bluetoothctl_log1"
echo "$bluetoothctl_log2"
echo "$bluetoothctl_log3"

echo " "
echo " "


