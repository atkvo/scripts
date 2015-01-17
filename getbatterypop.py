#!/usr/bin/env python3

import sys
import subprocess

def main():
    #batTime = subprocess.check_output("cat /sys/class/power_supply/BAT0/")
    batACPI = subprocess.check_output("acpi")
    batACPI = batACPI.decode()
    batACPI = batACPI.rstrip('\n')
#    batTime = batTime.decode()
#    batTime = batTime.rstrip('\n')
    #print(batACPI)
    commandDzen = '| dzen2 -p -x "1500" -y "30" -w "420" -l "5" -xs 1 -sa \'l\' -ta \'c\'\
    -title-name \'popup_batinfo\' -e \'onstart=uncollapse;button1=exit;button3=exit\''
    command = "(echo \"BATTERY STATUS\"\n"
    command = command + "echo " + '\"' + batACPI + '\"' + commandDzen + ")"
    #subprocess.call('echo \"BATTERY STATUS\"' + commandDzen, shell=True)
    subprocess.call(command, shell=True)


if __name__ == "__main__":
    main()
