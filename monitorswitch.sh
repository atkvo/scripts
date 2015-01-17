#!/bin/bash

# Multi monitor switch around with keypress (only cycles through connnected)

#!/bin/bash
#
#A script to cycle through various display options
#
#

#Check whether internal or external monitors
#are connected and on.
INTERNAL=`xrandr | grep -c "LVDS1 connected 1600x900"`
EXTERNAL=`xrandr | grep -c "HDMI1 connected 1920x1080"`

#Some math to make things unique
if [ $EXTERNAL = 1 ]; then
    EXTERNAL=3
fi

STATUS=$(($EXTERNAL+$INTERNAL))
#Possible status values:
#'1' -- indicates internal is on
#'3' -- indicates external is on
#'4' -- indicates both are on
echo "$STATUS"
case $STATUS in
#Current rotation: internal, both, external, repeat

    1 ) #Internal on, switch to both
    bspdual.sh
    ;;

    3 ) #External on, switch to laptop
    xrandr --output VGA1 --off
    xrandr --output HDMI1 --off
    sleep 1s
    xrandr --output LVDS1 --mode 1600x900
    ;;

    4 ) #Both on, switch to external
    bspdual.sh
    ;;

esac

#In case used as part of docking -- rerun xmodmap
#xmodmap ~/.Xmodmap

exit 0
