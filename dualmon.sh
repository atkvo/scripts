#!/bin/bash


if [[ -z `xrandr | grep " connected" | grep 'VGA'` ]]; then
	echo "No external monitor found" &
	xrandr --output LVDS1 --auto &
	# bspc monitor -d I II III IV &
else
	# xrandr --output LVDS1 --off &
	# xrandr --output VGA1 --auto &
        # xrandr --output VGA1 --mode 1920x1080 --left-of HDMI1 &
	# xrandr --output HDMI1 --auto &
	# xrandr --output HDMI1 --mode 1920x1080 &
	# xrandr --output HDMI1 --right-of VGA1 &
	# (sleep 1s && xrandr --output LVDS1 --off) &
	# (sleep 1s && xrandr --output HDMI1 --auto) &
	# (sleep 1s && xrandr --output VGA1 --mode 1920x1080 --left-of HDMI1) &
	# xrandr --output LVDS1 --off --output HDMI1 --auto --pos 1080x455 --output VGA1 --mode 1920x1080 --rotate right --left-of HDMI1 &
    # xrandr --output HDMI1 --pos 1080x455
    xrandr --output HDMI1 --auto --output VGA1 --auto --left-of HDMI1
	# bspc monitor HDMI1 -n MAIN -d I II III
	# bspc monitor VGA1 -n ALT -d IV V VI &
fi
