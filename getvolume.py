#!/usr/bin/env python3

import sys
import subprocess

def drawbars(p):
    BARS_MAX = 20
    # [####################]
    # 5 VOLUME PER #
    if p == 'm':
        x = '['
        for i in range(BARS_MAX):
            x = x + '_'
            #x = x + chr(215)
        x = x + ']'
    elif p == 0:
        x = '['
        for i in range(BARS_MAX):
            x = x + ' '
        x = x + ']'
    else:        
        percent = float(int(p)/100)
        bars = round(percent * float(BARS_MAX))
        x = '['
        for i in range(BARS_MAX):
            if i >=  bars:
                x = x + ' '
            else:
                #x = x + '*'
                x = x + chr(164)
        x = x + ']'
    print(x)

def writepercent(p):
    if p == 'm':
        x = "muted"
    elif p == 0:
        x = '00'
    else:
        x = int(p)
        if x < 10:
            x = '0' + (p)
        else:
            x = p
    print(x)

def main():
    p = subprocess.Popen("pamixer --get-mute", shell=True, stdout=subprocess.PIPE)
    p.wait()
    m = p.returncode
    #print(m)
    if m == 0:
        #print("VOLUME: --")
        #drawbars('m')
        writepercent('m')
    else:
        try:
            x = subprocess.check_output("pamixer --get-volume", shell=True)
            x = x.decode()
            x = x.rstrip('\n')
        except:
            x = 0
        #drawbars(x)
        writepercent(x)
        #print("VOLUME:", x)

if __name__ == "__main__":
    main()

