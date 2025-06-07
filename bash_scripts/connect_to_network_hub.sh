#!/bin/bash

network_hub_BSSID="FC:8B:97:70:28:C9"
network_hub_SSID="DTF"
network_hub_PASSWORD="jrQ10s7Kt8"
cred1="admin"
cred2="admin"

echo " "
sudo nmcli device wifi connect "$network_hub_BSSID" password "$network_hub_PASSWORD"
echo " "
echo "Connected to $network_hub_SSID"

echo " "
echo " "


