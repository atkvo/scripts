#!/bin/bash


if [[ -z `xrandr | grep " connected" | grep 'VGA'` ]]; then
	echo "No external monitor found" &
	xrandr --output LVDS1 --auto &
	bspc monitor -d I II III IV &
else
	# xrandr --output LVDS1 --off &
	# xrandr --output VGA1 --auto &
 #      xrandr --output VGA1 --mode 1920x1080 --left-of HDMI1 &
	# xrandr --output HDMI1 --auto &
	# xrandr --output HDMI1 --mode 1920x1080 &
	# xrandr --output HDMI1 --right-of VGA1 &
	/home/avo/scripts/dualmon.sh &
	# bspc monitor HDMI1 -n MAIN -d I II III
	# bspc monitor VGA1 -n ALT -d IV V VI &
	bspc monitor HDMI1 -n MAIN -d I II III &
	bspc monitor VGA1 -n ALT -d IV V VI &
	# bspc monitor -d I II III IV V VI &
fi
