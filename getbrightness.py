#!/usr/bin/env python3

import sys
import subprocess

# Update to use cat instead?
def drawbars(p):
    BARS_MAX = 20
    # [####################]
    # 5 VOLUME PER #
    if p == 0:
        x = 'BRIGHT ['
        for i in range(BARS_MAX):
            x = x + '_'
        x = x + ']'
    else:
        percent = float(int(p)/100)
        bars = round(percent * float(BARS_MAX))
        x = 'BRIGHT ['
        for i in range(BARS_MAX):
            if i >=  bars:
                x = x + ' '
            else:
                #x = x + '*'
                x = x + chr(164)
        x = x + ']'
    print(x)


def main():
    x = float(subprocess.check_output("xbacklight -get", shell=True))
    x = round(x)
    drawbars(x)
    #if x == 0:
    #    print("----")
    #    pass
    #else:
    #    print("LUMEN: ", x, "%")


if __name__ == "__main__":
    main()
