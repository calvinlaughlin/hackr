import curses
import sys
import time
import random

# new array of 10 mazes
# maze size in maze generator is 12x19 with 'O' as wall
# maze gen url: https://www.dcode.fr/maze-generator
# add quotes and commas url: https://onlinetexttools.com/add-quotes-to-lines
mazes = [
    ["OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "=S       O  O     O  O        O     O",
    "OOOO  OOOO  O  O  O  O  OOOOOOOOOO  O",
    "O              O           O     O  O",
    "OOOOOOO  OOOOOOOOOOOOOOOO  OOOO  O  O",
    "O  O     O  O        O           O  O",
    "O  O  O  O  OOOO  O  O  OOOO  O  O  O",
    "O     O     O  O  O  O  O     O  O  O",
    "OOOOOOOOOO  O  O  OOOO  OOOO  OOOO  O",
    "O  O        O           O           O",
    "O  O  OOOOOOOOOO  O  OOOO  O  OOOO  O",
    "O        O  O     O  O  O  O  O  O  O",
    "O  OOOOOOO  OOOO  OOOO  OOOOOOO  O  O",
    "O  O        O  O  O     O     O     O",
    "O  O  OOOOOOO  OOOO  OOOO  OOOOOOO  O",
    "O     O  O     O                    O",
    "OOOO  O  O  OOOO  OOOO  O  O  OOOO  O",
    "O     O     O  O  O     O  O  O  O  O",
    "O  OOOO  O  O  OOOOOOOOOOOOO  O  O  O",
    "O  O     O  O                    O  O",
    "OOOOOOO  OOOOOOO  OOOO  OOOO  O  O  O",
    "O  O     O  O  O  O  O     O  O  O  O",
    "O  OOOO  O  O  O  O  O  O  OOOO  OOOO",
    "O  O  O        O  O     O     O     O",
    "O  O  O  OOOO  OOOOOOOOOOOOO  OOOO  O",
    "O     O  O  O  O  O  O     O     O  O",
    "OOOO  O  O  OOOO  O  O  OOOOOOO  O  O",
    "O     O     O           O        O  O",
    "O  OOOOOOO  OOOOOOO  O  O  OOOO  O  O",
    "O  O  O        O  O  O        O  O  O",
    "O  O  O  O  OOOO  OOOOOOO  O  OOOOOOO",
    "O        O                 O  O     O",
    "O  OOOOOOOOOO  O  OOOO  OOOOOOO  OOOO",
    "O     O        O  O                 O",
    "O  OOOOOOO  OOOOOOOOOOOOO  OOOOOOO  O",
    "O  O        O  O  O        O  O     O",
    "O  O  OOOOOOO  O  OOOO  OOOO  O  O  O",
    "O  O                 O     O     O E=",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",],
    
    ["OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "=S O                       O  O  O  O",
    "O  OOOO  O  O  OOOO  OOOOOOO  O  O  O",
    "O        O  O  O  O        O     O  O",
    "O  OOOOOOOOOO  O  OOOOOOOOOO  OOOO  O",
    "O     O     O     O     O        O  O",
    "O  OOOOOOO  O  OOOOOOO  O  O  OOOO  O",
    "O  O     O              O  O  O     O",
    "O  O  OOOO  OOOO  OOOO  O  OOOO  OOOO",
    "O     O     O        O  O        O  O",
    "OOOO  OOOOOOOOOOOOOOOO  OOOO  OOOO  O",
    "O  O  O  O  O  O  O  O  O  O        O",
    "O  O  O  O  O  O  O  O  O  O  O  O  O",
    "O           O  O           O  O  O  O",
    "OOOO  OOOO  O  OOOO  O  O  O  OOOOOOO",
    "O  O     O     O  O  O  O           O",
    "O  O  O  OOOO  O  OOOOOOO  O  O  O  O",
    "O     O  O     O        O  O  O  O  O",
    "OOOO  O  OOOOOOO  O  OOOO  OOOOOOO  O",
    "O  O  O  O  O     O     O     O  O  O",
    "O  OOOOOOO  O  O  OOOO  O  OOOO  O  O",
    "O  O  O        O  O           O     O",
    "O  O  OOOO  OOOOOOOOOOOOO  O  O  O  O",
    "O     O        O     O  O  O  O  O  O",
    "OOOO  OOOOOOOOOO  OOOO  O  OOOO  O  O",
    "O        O     O        O     O  O  O",
    "O  OOOO  O  OOOO  OOOO  O  OOOO  OOOO",
    "O     O  O     O     O  O     O  O  O",
    "O  OOOO  O  OOOOOOO  OOOOOOOOOO  O  O",
    "O  O  O              O     O  O     O",
    "OOOO  OOOOOOOOOO  OOOOOOO  O  O  O  O",
    "O     O  O        O        O     O  O",
    "O  OOOO  OOOO  O  O  OOOO  OOOOOOO  O",
    "O              O  O  O     O        O",
    "O  O  OOOOOOO  OOOOOOOOOO  O  O  OOOO",
    "O  O     O  O     O     O     O  O  O",
    "OOOO  O  O  OOOO  O  OOOO  OOOO  O  O",
    "O     O     O                 O    E=",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",],
    
    ["OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "=S    O     O     O     O        O  O",
    "OOOO  O  OOOO  OOOO  O  OOOO  OOOO  O",
    "O     O           O  O           O  O",
    "O  OOOOOOO  OOOOOOOOOOOOOOOOOOO  O  O",
    "O              O  O  O     O     O  O",
    "O  OOOOOOO  OOOO  O  O  OOOO  OOOO  O",
    "O        O        O  O              O",
    "OOOOOOO  O  O  O  O  O  OOOOOOO  O  O",
    "O        O  O  O  O        O     O  O",
    "OOOOOOOOOO  OOOO  O  OOOOOOO  OOOOOOO",
    "O        O  O        O  O     O     O",
    "OOOO  OOOOOOOOOO  OOOO  O  O  OOOO  O",
    "O     O        O     O     O        O",
    "O  OOOOOOO  OOOO  O  OOOOOOOOOO  OOOO",
    "O           O     O     O     O  O  O",
    "O  OOOOOOOOOO  O  OOOOOOO  O  OOOO  O",
    "O     O     O  O     O     O     O  O",
    "OOOO  OOOO  OOOO  O  O  OOOO  OOOO  O",
    "O     O     O     O        O  O  O  O",
    "OOOO  OOOO  O  OOOOOOOOOOOOOOOO  O  O",
    "O  O  O           O  O  O           O",
    "O  O  O  O  O  OOOO  O  O  O  OOOOOOO",
    "O        O  O        O  O  O        O",
    "O  O  OOOOOOO  OOOOOOO  O  OOOOOOO  O",
    "O  O  O     O  O              O  O  O",
    "O  OOOOOOO  O  OOOO  OOOOOOOOOO  OOOO",
    "O     O  O        O  O        O     O",
    "OOOOOOO  OOOO  OOOO  OOOOOOO  OOOO  O",
    "O  O           O              O     O",
    "O  O  O  OOOO  O  OOOO  O  O  O  OOOO",
    "O     O  O        O  O  O  O  O  O  O",
    "O  O  OOOO  OOOOOOO  O  OOOOOOO  O  O",
    "O  O  O  O  O  O           O        O",
    "O  OOOO  O  O  OOOO  O  O  O  OOOOOOO",
    "O  O  O        O  O  O  O  O        O",
    "OOOO  OOOO  OOOO  O  OOOO  OOOO  OOOO",
    "O           O           O          E=",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",],
    
    ["OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "=S O     O  O  O              O     O",
    "O  OOOO  O  O  O  O  OOOOOOO  O  O  O",
    "O  O        O     O     O        O  O",
    "O  OOOOOOO  OOOOOOO  OOOO  OOOOOOOOOO",
    "O     O  O  O     O  O           O  O",
    "O  OOOO  O  O  OOOOOOO  OOOOOOOOOO  O",
    "O     O  O     O                    O",
    "O  OOOO  O  OOOO  OOOO  O  O  OOOOOOO",
    "O     O     O        O  O  O     O  O",
    "O  OOOOOOO  O  O  O  OOOO  O  O  O  O",
    "O              O  O  O  O  O  O     O",
    "O  OOOOOOOOOOOOOOOOOOO  OOOOOOO  OOOO",
    "O     O     O  O     O  O  O  O     O",
    "OOOO  OOOO  O  O  O  O  O  O  OOOO  O",
    "O     O           O     O     O  O  O",
    "O  OOOOOOO  OOOO  OOOOOOOOOO  O  OOOO",
    "O           O  O     O  O           O",
    "O  OOOOOOOOOO  OOOO  O  O  OOOOOOOOOO",
    "O        O        O     O  O  O     O",
    "O  OOOOOOO  O  OOOOOOO  O  O  O  OOOO",
    "O           O  O     O        O     O",
    "O  O  OOOO  OOOOOOO  OOOO  OOOO  OOOO",
    "O  O  O  O        O     O  O        O",
    "O  OOOO  O  OOOOOOO  O  OOOOOOOOOO  O",
    "O  O  O  O           O     O     O  O",
    "OOOO  O  O  OOOO  OOOOOOO  O  O  O  O",
    "O  O  O     O        O  O  O  O  O  O",
    "O  O  O  O  OOOO  OOOO  OOOO  OOOO  O",
    "O        O  O  O  O        O        O",
    "O  OOOO  OOOO  O  O  OOOO  O  OOOOOOO",
    "O  O        O  O     O  O  O        O",
    "O  OOOO  O  O  O  OOOO  O  OOOO  OOOO",
    "O  O  O  O     O     O  O           O",
    "OOOO  O  OOOOOOOOOO  O  OOOOOOOOOO  O",
    "O  O  O           O  O        O     O",
    "O  O  O  OOOOOOO  OOOOOOO  OOOO  O  O",
    "O        O                    O  O E=",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",],
    
    ["OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "=S    O           O        O        O",
    "OOOO  OOOOOOO  OOOO  OOOOOOO  OOOOOOO",
    "O           O  O  O     O  O        O",
    "OOOOOOO  OOOO  O  O  OOOO  O  OOOO  O",
    "O  O     O              O        O  O",
    "O  O  OOOO  OOOO  OOOOOOO  O  OOOOOOO",
    "O     O  O  O              O  O     O",
    "OOOO  O  O  O  O  OOOOOOOOOO  O  O  O",
    "O     O     O  O        O  O  O  O  O",
    "OOOO  O  OOOOOOOOOO  OOOO  O  O  OOOO",
    "O  O     O           O              O",
    "O  OOOO  OOOOOOO  O  O  O  OOOO  O  O",
    "O  O     O  O  O  O  O  O  O  O  O  O",
    "O  O  OOOO  O  O  OOOOOOO  O  OOOO  O",
    "O  O        O     O     O     O     O",
    "O  OOOO  O  OOOOOOOOOO  O  OOOO  OOOO",
    "O        O  O        O        O     O",
    "O  OOOO  OOOO  O  O  OOOO  OOOOOOO  O",
    "O  O     O  O  O  O        O        O",
    "O  O  O  O  OOOOOOOOOO  OOOOOOOOOO  O",
    "O  O  O        O        O  O        O",
    "OOOOOOOOOOOOOOOO  OOOO  O  O  OOOO  O",
    "O        O  O        O  O  O     O  O",
    "OOOO  O  O  OOOOOOO  OOOO  O  OOOOOOO",
    "O     O     O              O     O  O",
    "O  OOOO  OOOO  OOOO  OOOOOOOOOO  O  O",
    "O     O        O  O           O  O  O",
    "O  OOOO  O  OOOO  O  O  O  OOOO  O  O",
    "O     O  O        O  O  O     O  O  O",
    "O  O  OOOOOOOOOO  OOOOOOO  OOOOOOO  O",
    "O  O        O     O     O     O     O",
    "OOOOOOO  OOOO  OOOO  OOOO  O  O  OOOO",
    "O  O        O  O  O        O     O  O",
    "O  OOOOOOO  OOOO  OOOO  OOOO  OOOO  O",
    "O  O              O     O           O",
    "O  OOOO  OOOOOOOOOOOOOOOO  OOOO  O  O",
    "O                 O        O     O E=",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",],
    
    ["OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "=S    O  O  O  O           O     O  O",
    "O  OOOO  O  O  OOOO  OOOOOOOOOO  O  O",
    "O  O     O     O     O           O  O",
    "O  O  OOOO  OOOOOOO  O  OOOOOOO  O  O",
    "O              O        O     O  O  O",
    "O  O  O  OOOOOOOOOO  OOOO  O  OOOO  O",
    "O  O  O  O     O  O     O  O        O",
    "OOOO  OOOOOOO  O  OOOO  O  OOOOOOO  O",
    "O        O     O     O           O  O",
    "O  OOOO  O  OOOO  O  OOOOOOO  O  OOOO",
    "O     O     O     O  O     O  O  O  O",
    "OOOO  O  OOOO  OOOOOOO  OOOO  OOOO  O",
    "O  O  O                             O",
    "O  OOOO  OOOOOOOOOOOOOOOOOOO  OOOOOOO",
    "O           O  O  O              O  O",
    "OOOO  OOOOOOO  O  OOOOOOOOOOOOO  O  O",
    "O  O        O  O  O           O  O  O",
    "O  O  OOOO  O  O  O  OOOOOOOOOO  O  O",
    "O        O     O              O     O",
    "O  OOOO  O  OOOO  O  OOOOOOOOOO  OOOO",
    "O  O     O     O  O     O  O     O  O",
    "O  O  OOOO  OOOOOOO  OOOO  OOOO  O  O",
    "O  O  O     O  O           O        O",
    "O  OOOOOOO  O  OOOOOOO  OOOO  OOOO  O",
    "O  O        O     O  O     O  O     O",
    "O  OOOOOOO  OOOO  O  O  O  OOOOOOOOOO",
    "O  O  O  O     O        O  O        O",
    "OOOO  O  O  OOOOOOO  OOOOOOO  O  OOOO",
    "O  O  O     O        O  O  O  O     O",
    "O  O  O  OOOOOOOOOO  O  O  O  OOOO  O",
    "O        O  O           O     O  O  O",
    "OOOO  OOOO  OOOO  OOOOOOOOOOOOO  O  O",
    "O     O     O     O  O     O     O  O",
    "O  OOOOOOO  O  OOOO  OOOO  O  O  O  O",
    "O     O     O     O  O     O  O  O  O",
    "O  OOOO  O  O  OOOO  OOOO  OOOO  O  O",
    "O        O                         E=",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",],
    
    ["OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "=S O  O        O  O        O  O  O  O",
    "O  O  O  O  O  O  O  OOOOOOO  O  O  O",
    "O        O  O        O     O  O     O",
    "OOOOOOOOOO  OOOOOOOOOO  OOOO  OOOO  O",
    "O        O     O     O     O  O  O  O",
    "O  O  OOOO  O  OOOO  OOOO  O  O  O  O",
    "O  O  O     O  O        O           O",
    "OOOO  O  OOOOOOO  OOOO  OOOO  OOOO  O",
    "O              O  O           O  O  O",
    "O  O  OOOO  OOOOOOO  OOOOOOO  O  OOOO",
    "O  O  O  O                 O     O  O",
    "OOOOOOO  OOOO  O  OOOO  OOOOOOOOOO  O",
    "O     O        O  O              O  O",
    "O  O  O  O  OOOOOOOOOO  OOOOOOO  O  O",
    "O  O     O     O     O  O           O",
    "O  OOOOOOO  O  OOOO  O  O  O  O  OOOO",
    "O     O     O  O  O  O  O  O  O  O  O",
    "O  OOOOOOO  O  O  O  OOOOOOO  O  O  O",
    "O        O  O     O  O        O  O  O",
    "O  OOOOOOOOOOOOOOOO  OOOOOOO  O  O  O",
    "O              O  O        O  O     O",
    "O  OOOOOOO  OOOO  O  O  O  OOOO  OOOO",
    "O     O  O  O        O  O        O  O",
    "OOOOOOO  OOOOOOOOOO  O  OOOOOOOOOO  O",
    "O        O           O     O     O  O",
    "OOOO  O  O  O  OOOO  OOOOOOOOOO  O  O",
    "O     O  O  O     O        O     O  O",
    "OOOOOOO  OOOOOOO  O  O  OOOO  O  O  O",
    "O        O        O  O        O     O",
    "O  O  OOOO  O  OOOO  OOOO  O  OOOO  O",
    "O  O  O  O  O  O     O     O  O  O  O",
    "O  OOOO  OOOO  OOOOOOOOOOOOO  O  OOOO",
    "O     O  O     O           O        O",
    "OOOO  O  OOOO  O  O  O  OOOO  OOOO  O",
    "O     O     O  O  O  O        O     O",
    "OOOO  OOOO  OOOOOOO  O  O  O  O  OOOO",
    "O                    O  O  O  O    E=",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",],
    
    ["OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "=S          O     O           O  O  O",
    "O  O  O  OOOOOOO  O  OOOOOOOOOO  O  O",
    "O  O  O  O              O           O",
    "O  OOOO  O  OOOOOOOOOO  O  O  O  O  O",
    "O  O  O     O  O           O  O  O  O",
    "OOOO  OOOOOOO  OOOOOOO  OOOOOOOOOOOOO",
    "O  O           O     O     O        O",
    "O  OOOOOOOOOO  OOOO  O  OOOO  OOOO  O",
    "O           O                 O  O  O",
    "O  OOOOOOOOOO  O  OOOOOOO  OOOO  O  O",
    "O     O        O     O  O  O        O",
    "OOOO  O  O  OOOOOOO  O  OOOOOOO  O  O",
    "O     O  O  O  O  O     O        O  O",
    "OOOO  O  O  O  O  OOOOOOO  OOOOOOOOOO",
    "O        O           O        O     O",
    "O  OOOOOOO  OOOOOOOOOOOOO  OOOOOOO  O",
    "O        O              O  O     O  O",
    "O  O  O  OOOOOOO  O  OOOO  O  O  O  O",
    "O  O  O     O  O  O     O  O  O     O",
    "O  OOOO  O  O  OOOO  OOOO  O  OOOO  O",
    "O     O  O     O        O  O  O     O",
    "OOOO  O  OOOO  OOOOOOO  OOOO  O  OOOO",
    "O     O  O     O     O  O     O  O  O",
    "O  OOOO  OOOOOOO  OOOOOOO  OOOOOOO  O",
    "O  O        O  O              O     O",
    "O  OOOO  OOOO  O  OOOO  OOOO  OOOO  O",
    "O     O              O  O     O     O",
    "OOOO  OOOOOOOOOO  OOOO  OOOO  O  O  O",
    "O              O     O     O     O  O",
    "O  OOOO  OOOOOOOOOOOOO  OOOOOOOOOO  O",
    "O     O     O     O     O        O  O",
    "OOOO  OOOOOOO  OOOOOOOOOO  OOOO  OOOO",
    "O        O                 O     O  O",
    "O  O  OOOO  OOOO  O  O  O  OOOO  O  O",
    "O  O  O  O     O  O  O  O  O        O",
    "OOOO  O  OOOO  O  OOOOOOO  OOOO  OOOO",
    "O              O        O  O       E=",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
],
    
    ["OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "=S       O                          O",
    "O  OOOO  OOOO  OOOO  OOOOOOOOOOOOO  O",
    "O     O        O  O              O  O",
    "O  OOOOOOOOOOOOO  O  OOOOOOO  OOOOOOO",
    "O        O     O  O     O     O     O",
    "OOOOOOOOOO  O  O  OOOOOOO  OOOO  OOOO",
    "O     O     O  O        O     O  O  O",
    "O  OOOO  OOOOOOOOOOOOO  O  OOOO  O  O",
    "O     O     O              O        O",
    "O  OOOO  O  OOOOOOO  O  OOOOOOO  OOOO",
    "O        O  O        O     O        O",
    "O  O  O  OOOOOOOOOOOOO  OOOOOOO  OOOO",
    "O  O  O  O  O  O           O        O",
    "OOOO  O  O  O  O  OOOOOOOOOOOOOOOO  O",
    "O  O  O  O     O     O              O",
    "O  OOOO  O  OOOO  OOOO  OOOO  OOOOOOO",
    "O  O           O           O        O",
    "O  OOOO  O  OOOO  OOOOOOO  O  O  O  O",
    "O  O     O        O  O     O  O  O  O",
    "O  O  O  OOOOOOOOOO  OOOO  OOOOOOO  O",
    "O     O     O  O        O     O  O  O",
    "O  OOOO  OOOO  O  OOOO  O  O  O  OOOO",
    "O     O  O     O     O     O     O  O",
    "O  OOOOOOO  OOOO  O  OOOOOOOOOOOOO  O",
    "O     O           O  O     O  O     O",
    "O  OOOOOOO  OOOOOOO  O  OOOO  O  O  O",
    "O  O  O     O        O     O     O  O",
    "OOOO  O  OOOO  O  O  OOOO  OOOO  O  O",
    "O     O  O  O  O  O     O        O  O",
    "O  O  OOOO  OOOO  OOOO  OOOO  O  O  O",
    "O  O  O           O  O        O  O  O",
    "O  OOOOOOOOOO  OOOO  O  OOOOOOOOOO  O",
    "O           O  O  O     O  O  O     O",
    "OOOOOOOOOO  O  O  O  O  O  O  OOOO  O",
    "O           O  O     O     O        O",
    "O  O  OOOO  O  OOOOOOOOOO  OOOOOOO  O",
    "O  O  O              O     O       E=",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",],
    
    ["OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",
    "=S       O  O     O        O        O",
    "OOOO  OOOO  O  OOOO  OOOOOOOOOO  OOOO",
    "O           O           O           O",
    "O  OOOOOOOOOOOOO  O  OOOO  O  O  OOOO",
    "O           O     O        O  O     O",
    "O  OOOOOOOOOOOOO  O  OOOO  OOOOOOO  O",
    "O        O     O  O     O  O  O  O  O",
    "O  OOOOOOO  OOOOOOO  OOOOOOO  O  O  O",
    "O           O  O     O              O",
    "O  OOOO  O  O  OOOO  OOOOOOOOOOOOOOOO",
    "O     O  O        O  O              O",
    "OOOOOOO  O  O  O  O  OOOO  O  OOOO  O",
    "O     O  O  O  O           O     O  O",
    "O  OOOOOOO  OOOOOOOOOO  OOOOOOO  OOOO",
    "O     O        O  O           O     O",
    "O  OOOO  O  OOOO  O  O  OOOOOOOOOO  O",
    "O        O  O  O     O  O        O  O",
    "OOOO  O  OOOO  OOOOOOOOOOOOO  OOOO  O",
    "O  O  O  O                 O     O  O",
    "O  O  OOOOOOO  OOOOOOOOOOOOOOOO  O  O",
    "O           O        O              O",
    "OOOOOOO  OOOOOOOOOO  OOOO  OOOOOOOOOO",
    "O           O           O        O  O",
    "OOOO  O  OOOO  O  OOOO  O  OOOOOOO  O",
    "O  O  O  O  O  O     O  O  O  O     O",
    "O  O  O  O  O  O  OOOOOOOOOO  OOOO  O",
    "O  O  O        O                 O  O",
    "O  O  OOOOOOO  OOOOOOOOOO  O  O  O  O",
    "O     O                 O  O  O     O",
    "O  OOOOOOOOOOOOOOOO  OOOO  OOOOOOOOOO",
    "O     O        O  O  O              O",
    "O  O  O  O  O  O  OOOOOOOOOO  OOOO  O",
    "O  O  O  O  O                 O  O  O",
    "OOOOOOO  O  O  OOOOOOOOOOOOO  O  O  O",
    "O        O  O        O  O     O  O  O",
    "OOOO  OOOOOOOOOOOOOOOO  O  O  O  O  O",
    "O                    O     O  O    E=",
    "OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",],
]


def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.keypad(1)    # Enable special Key values
    stdscr.nodelay(1)   # Make getch non-blocking
    curses.noecho()     # Turn off auto-echoing of keypress on to screen
    curses.cbreak()     # React to keys instantly, without waiting for enter to be pressed
    h, w = stdscr.getmaxyx()
    
    # select random maze from mazes
    maze = mazes[random.randint(0, len(mazes)-1)]

    # translate the maze and all functionality to the right by this amount:
    x_translate = 90
    
    y, x = 1, 2 + x_translate  # Start position of new mazes
    previous_position = (y, x)

    # Initial drawing of the maze assuming window size is 130x40
    for i, row in enumerate(maze):
        stdscr.addstr(i, x_translate, row) # maze_x used to be 0 here
    stdscr.addstr(y, x, '@')
    stdscr.refresh()

    start_time = time.time()  # Start the timer
    duration = 120  # 2 minutes in seconds
    timer_x = x_translate - 15 # new position for the timer

    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    while True:
        remaining_time = max(0, duration - int(time.time() - start_time))
        mins, secs = divmod(remaining_time, 60)
        timer_str = f"Time: {mins:02}:{secs:02}"
        stdscr.addstr(1, timer_x, timer_str)  # Display timer

        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(1, timer_x, timer_str)
        stdscr.attroff(curses.color_pair(1))

        key = stdscr.getch()
        stdscr.addstr(y, x, ' ')  # Clear the old player position

        # Determine the action based on key press
        if key == curses.KEY_UP and maze[y-1][x - x_translate] not in ['-', '|', '+', 'O']:
            y -= 1
        elif key == curses.KEY_DOWN and maze[y+1][x - x_translate] not in ['-', '|', '+', 'O']:
            y += 1
        elif key == curses.KEY_LEFT and maze[y][x-1 - x_translate] not in ['-', '|', '+', 'S', 'O']:
            x -= 1
        elif key == curses.KEY_RIGHT and maze[y][x+1 - x_translate] not in ['-', '|', '+', 'O']:
            x += 1
        elif key == ord('q'):  # Quit the game
            break

        # Redraw the player at the new position
        stdscr.addstr(y, x, '@')
        stdscr.refresh()  # Minimize the use of refresh

        # Check if the player has reached the exit
        if maze[y][x - x_translate] == 'E':
            stdscr.addstr(h//2, w//2 - len("You won!")//2, "You won!")
            stdscr.refresh()
            stdscr.getch()
            break
        
        # Check if time's up
        if remaining_time <= 0:
            stdscr.addstr(h//2, w//2 - len("Time's up!")//2, "Time's up!")
            stdscr.refresh()
            stdscr.getch()
            # this could be sys.exit(100) to exit the program, but for now break
            break
    stdscr.clear()
            

if __name__ == "__main__":
    curses.wrapper(main)
