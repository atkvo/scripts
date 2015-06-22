#!/bin/bash

#j4-dmenu-desktop --dmenu='dmenu -i -l 10 -fn Droid\ Sans-10 -nb black -nf white -sb white -sf black' --term='myterminal.sh'
#FONT='Terminus-9'
FONT='Tewi-11'
BG='"#1d1f21"'
FG='"#C5C8C6"'
#j4-dmenu-desktop --dmenu='dmenu -i -l 20 -fn '$FONT' -nb '$BG' -nf '$FG' -sb white -sf '$BG' -dim 0.8 -w 400 -x 100 -y 100' --term='myterminal.sh'
j4-dmenu-desktop --dmenu='dmenu -i -l 20 -fn '$FONT' -nb '$BG' -nf '$FG' -sb white -sf '$BG' -w 400 -x 100 -y 100' --term='myterminal.sh'
