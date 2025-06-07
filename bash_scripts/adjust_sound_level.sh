#!/bin/bash

amixerlog1=$(amixer | grep "Simple mixer control")
echo "$amixerlog1"

Audiocontroller="Master"
amixer sset "$Audiocontroller" 80%

echo " "
echo " "


