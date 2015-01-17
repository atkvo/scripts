#!/usr/bin/env python3

import subprocess

def main():
    x = subprocess.check_output("xprop -root _NET_CURRENT_DESKTOP | sed -e 's/_NET_CURRENT_DESKTOP(CARDINAL) = //'", shell=True)
    x = x.decode()
    x = x.rstrip('\n')
    x = int(x) + 1
    print(chr(171), x,chr(187))
    
if __name__ == '__main__':
    main()
