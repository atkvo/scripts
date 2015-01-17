#!/bin/bash

BATINFO=$(acpi -b | sed -e s/'Battery 0:'//)

(
echo "BATTERY INFO"
echo "$BATINFO"
) | dzen2 -p -x "1500" -y "30" -w "320" -l "2" -xs 1 -sa 'c' -ta 'c'\
    -title-name 'popup_sysinfo' -e 'onstart=uncollapse;button1=exit;button3=exit'
