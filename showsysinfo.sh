#!/bin/bash



TIMEDATE="\n$(date +"%r -- %a %B %d %Y")"

# Get volume
if [ "$(pactl list sinks | grep Mute | awk '{print $2}')" ==  "no" ] 
then
	VOL="\n\nVolume: $(pactl list sinks | grep "Volume: f" | awk '{print $5}')"
else
	VOL="\n\nVolume: muted"
fi

# Get Battery information
BATTERY=$(acpi)
BATTERY=${BATTERY##Battery 0:}
BATTERY=${BATTERY%%, rate information unavailable}
BATTERY="\n\nBattery: $BATTERY"

# Create notification string
NOTIFSTRING=$TIMEDATE$VOL$BATTERY

#notify-send 'HI' 'Example notif.' --icon=dialog-information
#notify-send 'System Stats'  "$BATTERY" --icon=dialog-information &
notify-send 'System Stats'  "$NOTIFSTRING" --icon=dialog-information &


