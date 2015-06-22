#!/bin/sh

WMNAME=$XDG_CURRENT_DESKTOP
TESTNAME='bspwm'

echo $WMNAME

if [[ "$WMNAME" == "$TESTNAME" ]]; then
	echo "i3"
else
	echo "what"
fi
