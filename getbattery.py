#!/usr/bin/env python3

import sys
import subprocess

def drawbars(p, t):
    BARS_MAX = 10
    if p == 0:
        x = 'BATT ['
        for i in range(BARS_MAX):
            x = x + '_'
        x = x + ']'
    else:        
        percent = float(int(p)/100)
        bars = round(percent * float(BARS_MAX))
        x = 'BAT ['
        for i in range(BARS_MAX):
            if i >=  bars:
                x = x + ' '
            else:
                x = x + t
        x = x + ']'
    print(x)


def main():
    x = subprocess.check_output("acpi", shell=True)
    x = x.decode()
    x = x.rstrip('\n')
    x = x.rstrip('%')
    if x[11] == 'C':
        if x[26] == 'c':
#            print("CHRGING", x[21:24])
            percent = x[21:23]
            drawbars(percent, '+')
        else:
#            print("CHRGING", x[21:24], " TIME LEFT:", x[26:34])
            percent = x[21:23]
            drawbars(percent, '+')
    elif x[11] == 'U':
#        print("CHRGED", x[20:24])
        percent = x[20:23]
        drawbars(percent, '*')
    elif x[11] == 'F':
#        print("CHRGED", x[17:24])
        percent = x[17:20]
        drawbars(percent, '*')
    else:
        percent = x[24:26]
        drawbars(percent, '-')
        #print("DISCHRGING", x[24:27], " TIME LEFT:", x[29:38])
        


if __name__ == "__main__":
    main()
