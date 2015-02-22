#!/bin/bash



TIMEDATE="\n$(date +"%r -- %a %B %d %Y")"

# Get Battery information
BATTERY=$(acpi)
BATTERY=${BATTERY##Battery 0:}
BATTERY=${BATTERY%%, rate information unavailable}
BATTERY="\n\nBattery: $BATTERY"

# Create notification string
NOTIFSTRING=$TIMEDATE$BATTERY

#notify-send 'HI' 'Example notif.' --icon=dialog-information
#notify-send 'System Stats'  "$BATTERY" --icon=dialog-information &
notify-send 'System Stats'  "$NOTIFSTRING" --icon=dialog-information &


