#!/bin/bash

ifconfiguration_log1=$(ifconfig | grep "lo:")
ifconfiguration_log2=$(ifconfig | grep "wlp9s0:")

if [ ${#ifconfiguration_log1} != 0 ]
	then
		echo "Network first Communication Protocol is On"
	else
		echo "Network first Communication Protocol is Off"
fi

if [ ${#ifconfiguration_log2} != 0 ]
	then
		echo "Network second Communication Protocol is On"
	else
		echo "Network second Communication Protocol is Off"
fi

echo " "
echo " "


