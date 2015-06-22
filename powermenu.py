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
    option = _Getch()

    if option == 'u' or option == 'U':
        print('\n\t Are you sure? Y/N')
        option = _Getch()
        if option == 'y' or option == 'Y':
            print('\n\t GOODBYE! ')
            # subprocess.call(["shutdown", "-h" ,"now"])
            # subprocess.call(["systemctl", "poweroff" ])
            subprocess.call(["poweroff"])
        else:
            print("\tSHUTDOWN ABORTED")

    elif option == 'r' or option == 'R':
        print('\n\t Are you sure? Y/N')
        option = _Getch()
        if option == 'y' or option == 'Y':
            print('\n\t BE RIGHT BACK! ')
            subprocess.call(["shutdown", "-r" ,"now"])
        else:
            print("\tREBOOT ABORTED")

    elif option == 's' or option == 'S':
        print('\n\t NAP TIME! ')
        subprocess.call(["systemctl", "suspend"])

    else:
        print("ABORTED")
    

if __name__ == "__main__":
    main()
