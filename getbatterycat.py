#!/usr/bin/env python3

import sys
import subprocess

def drawbars(p, t):
    BARS_MAX = 20
    if p == 0:
        x = '['
        for i in range(BARS_MAX):
            x = x + '_'
        x = x + ']'
    else:        
        percent = float(int(p)/100)
        bars = round(percent * float(BARS_MAX))
        x = '['
        for i in range(BARS_MAX):
            if i >=  bars:
                x = x + ' '
            else:
                x = x + t
        x = x + ']'
    print(x)


def main():
    batFull = subprocess.check_output("cat /sys/class/power_supply/BAT0/energy_full", shell=True)
    batNow = subprocess.check_output("cat /sys/class/power_supply/BAT0/energy_now", shell=True)
    batStat = subprocess.check_output("cat /sys/class/power_supply/BAT0/status", shell=True)
    batFull = batFull.decode()
    batFull = batFull.rstrip('\n')
    batNow = batNow.decode()
    batNow = batNow.rstrip('\n')
    batStat = batStat.decode()
    batStat = batStat.rstrip('\n')


    batPercent = 100*(float(batNow)/float(batFull))
    batPercent = round(batPercent)
#    print(batFull, batNow, batStat, batPercent)
    
    if batStat == "Full" or batStat == "Unknown":
        #drawbars(100, '*')
        drawbars(100, chr(164))
    elif batStat == "Discharging":
        drawbars(batPercent, '-')
    elif batStat == "Charging":
        drawbars(batPercent, '+')


if __name__ == "__main__":
    main()
