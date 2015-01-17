#!/bin/bash

BATCHARGE=$(/home/avo/scripts/getbatterycat.py)
BRIGHTNESS=$(/home/avo/scripts/getbrightness.py)
WORKSPACE=$(/home/avo/scripts/getworkspace2bwm.py)
VOLUME=$(/home/avo/scripts/getvolume.py)
DATE=$(date +"%a %b %d %r")

trap "i=11" SIGUSR1;

i=0
n=0

while true; do
if [ $i -ge 10 ]
then 
    BATCHARGE=$(/home/avo/scripts/getbatterycat.py)
    BRIGHTNESS=$(/home/avo/scripts/getbrightness.py)
    VOLUME=$(/home/avo/scripts/getvolume.py)
    i=0
fi
if [ $n -ge 2 ]
then 
    DATE=$(date +"%a %b %d %r")
    n=0
fi

WORKSPACE=$(/home/avo/scripts/getworkspace2bwm.py)

echo "^fg()$WORKSPACE   ^fg()VOLUME $VOLUME ^fg() $BRIGHTNESS ^fg() BATTERY $BATCHARGE ^fg()$DATE "

sleep 0.5

let "i += 1"
let "n += 1"
done

