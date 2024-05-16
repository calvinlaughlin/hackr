import curses
import random
import time
import pygame
import subprocess
from maze import main as maze_main
from dialogue import stream_text
from matrix import matrix_wash, decay_from_top

import curses

def enter_name(stdscr):
    curses.curs_set(1)  # Show the cursor
    stdscr.clear()
    stdscr.refresh()

    stdscr.addstr(0, 0, "Please enter your name: ")
    stdscr.refresh()

    curses.echo()  # Enable echoing of characters

    name = ""
    while True:
        char = stdscr.getch()
        if char == curses.KEY_ENTER or char in [10, 13]:
            break
        elif char == curses.KEY_BACKSPACE or char == 127:
            name = name[:-1]
            y, x = stdscr.getyx()
            stdscr.move(y, x - 1)
            stdscr.delch()
        else:
            name += chr(char)

    curses.noecho()  # Disable echoing of characters
    curses.curs_set(0)  # Hide the cursor

    return name


def new_ui():
    t1 = [
        ('[NAME], what took you so fucking long? We don’t have much time left.       ', 'Wolfe'),
        ('I’m in position. I can practically smell that vault from here.             ', 'Wolfe'),
        ('First thing, though, I need you to chart me a path through these air vents.', 'Wolfe'),  
        ('I’m completely fuckin lost.                                                ', 'Wolfe'),
        ('Get in the security panel and find me a way out of this fuckin rat maze.   ', 'Wolfe')
    ]
    t2 = [
        ('Ok, I’m in position.                                                                                       ', 'Wolfe'),
        ('Waiting for a guard to pass under me… (talking to self) yeah you fuckin’ scum get outta here.              ', 'Wolfe'),
        ('Alright I’m making my through to the server room to disable the cameras for the rest of the team to get in.', 'Wolfe'),
        ('This place is a bloody fortress.                                                                           ', 'Wolfe'),
        ('Shit mate, there’s a keypad here to get into the server room.                                              ', 'Wolfe'),
        ('I need you to hack into the keypad to get me in.                                                           ', 'Wolfe'),
        ('It looks like you’ve only got four tries.                                                                  ', 'Wolfe'),
    ]
    t3 = [
        ('Alright, I’m in. Good shit working through that keypad. Now I’m in the server room.                    ', 'Wolfe'),
        ('Let me just open this laptop…                                                                          ', 'Wolfe'),
        ('Type the password in…                                                                                  ', 'Wolfe'),
        ('Click on this link to download the mainframe, OH SHIT I downloaded a virus, help me get rid of it mate!', 'Wolfe'),
    ]
    t4 = [
        ('', 'Wolfe'),
        ('', 'Wolfe'),
        ('', 'Wolfe'),
        ('', 'Wolfe'),
    ]
    t5 = [
        ('', 'Wolfe'),
        ('', 'Wolfe'),
        ('', 'Wolfe'),
        ('', 'Wolfe'),
    ]


    curses.wrapper(stream_text, t1)
    curses.endwin()

    # Run the maze.py script after the dialogue
    # subprocess.run(["python3", "maze.py"], check=True)
    curses.wrapper(maze_main)
    curses.wrapper(stream_text, t2)
    
    subprocess.run(["python3", "fallout.py"], check=True)
    curses.wrapper(stream_text, t3)
    
    subprocess.run(["python3", "pop-ups.py"], check=True)
    curses.wrapper(stream_text, t4)
    subprocess.run(["python3", "quick.py"], check=True)
    curses.wrapper(stream_text, t5)
    
def diego_story():
    # place to add in the dialogue/flow of the storyline diego came up with 
    messages = [
        ('What took you so fucking long? We don\'t have much time left.  ', 'Reznov'),
        ('Next one\'s all you. Should be simple. You crack it, we\'re in.', 'Reznov'),
        ('Ready? Of course you are. Let\'s finish this job.              ', 'Reznov')
    ]
    curses.wrapper(stream_text, messages)
    curses.endwin()
    
    # Run the maze.py script after the dialogue
    subprocess.run(["python3", "maze.py"], check=True)
    subprocess.run(["python3", "fallout.py"], check=True)
    subprocess.run(["python3", "pop-ups.py"], check=True)
    subprocess.run(["python3", "quick.py"], check=True)

def main(stdscr):
    # Turn off cursor blinking
    curses.curs_set(0)

    # Color setup
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

    selected_idx = 0
    options = ["Start", "Options"]

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Print the title
        stdscr.addstr(height // 3, (width - len("hackOS")) // 2, "hackOS", curses.A_BOLD)

        # Display the options
        for idx, option in enumerate(options):
            x = height // 2 + idx
            y = (width - len(option) - 2) // 2
            if idx == selected_idx:
                stdscr.addstr(x, y, "> " + option, curses.A_BOLD)
            else:
                stdscr.addstr(x, y, "  " + option)

        # Refresh the screen
        stdscr.refresh()

        # Wait for user input
        key = stdscr.getch()

        if key == curses.KEY_UP and selected_idx > 0:
            selected_idx -= 1
        elif key == curses.KEY_DOWN and selected_idx < len(options) - 1:
            selected_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            break

    # Execute the selected option
    if selected_idx == 0:
        matrix_wash(stdscr)
        decay_from_top(stdscr)
        username = enter_name(stdscr)
        new_ui()
    elif selected_idx == 1:
        pass

if __name__ == "__main__":
    curses.wrapper(main)
