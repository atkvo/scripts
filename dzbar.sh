#!/bin/sh
FONT='Tewi:pixelsize=12'
#FONT='Terminus:pixelsize=10'
#FONT='-*-proggycleanszbp-*-*-*-*-13-*-*-*-*-*-*-*'
#FONT='Profont:pixelsize=12'
#FONT='ProggyClean:pixelsize=12'
#FG='#FFFFFF'
#conky | dzen2 -e - -h '16' -w '600' -ta r -fn $FONT -xs 1 &
#/home/avo/scripts/getstats.sh | dzen2 -e - -h '25' -ta r -fn $FONT -xs 1 &
#/home/avo/scripts/getstats.sh | dzen2 -e 'onstart=lower;' -h '25' -ta r -fn $FONT -xs 1 &
/home/avo/scripts/getstats.sh | dzen2 -e 'onstart=lower;' -w '650' -h '25' -x 650 -ta r -fn $FONT -xs 1 &


