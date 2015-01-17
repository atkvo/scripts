#!/usr/bin/env python3

import sys
import subprocess
import tty
import termios

def _Getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def main():
    #option = input('SH(U)TDOWN, (R)ESTART, (S)LEEP')
    #print('|-- POWER OPTIONS ---------------|')
    #print('|--------------------------------|')
    #print('| SH[U]TDOWN, [R]ESTART, [S]LEEP |')
    #print('|--------------------------------|')
    print('\n\
               _________________              \n\
            __/  POWER OPTIONS  \____________ \n\
            |--------------------------------|\n\
            |                                |\n\
            |          SH[U]TDOWN            |\n\
            |            [R]EBOOT            |\n\
            |            [S]LEEP             |\n\
            |                                |\n\
            |________________________________|\n\
         ')
#     option = sys.stdin.read(1)
    option = _Getch()

    if option == 'u' or option == 'U':
        print('\n\t GOODBYE! ')
        subprocess.call(["sudo", "shutdown", "-h" ,"now"])
    elif option == 'r' or option == 'R':
        print('\n\t BE RIGHT BACK! ')
        subprocess.call(["sudo", "shutdown", "-r" ,"now"])
    elif option == 's' or option == 'S':
        print('\n\t NAP TIME! ')
        subprocess.call(["sudo", "pm-suspend"])
    else:
        print("ABORTED")
    

if __name__ == "__main__":
    main()
