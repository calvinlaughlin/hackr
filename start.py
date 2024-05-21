import curses
import random
import time
import pygame
import subprocess
from dialogue import stream_text, enter_name, display_computer_text, enter_account_number, display_progress_bar, print_large_message
from matrix import matrix_wash, decay_from_top
from maze import main as maze_main
# from quick import main as quick_main
# from pop_ups import main as pop_ups_main
# from fallout import main as fallout_main
from impossible import typing_puzzle

import curses

# GLOBAL VARS
USERNAME = 'ANONYMOUS'

# PUZZLE TEST BED
def new_ui(stdscr, username='ANONYMOUS'):    
    # text for the dialogue
    t1 = [
        (f'{username}, what took you so fucking long? We don’t have much time left.       ', 'Wolfe'),
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
        ('blah blah blah... on to the next puzzle that tests your agility', 'Wolfe')
    ]
    t5 = [
        ('nice job! this is the end of the puzzle test bed', 'Wolfe')
    ]

    curses.wrapper(stream_text, t1)
    curses.endwin()

    # Run the maze.py script after the dialogue
    # subprocess.run(["python3", "maze.py"], check=True)
    curses.wrapper(maze_main)
    curses.wrapper(stream_text, t2)
    
    subprocess.run(["python3", "fallout.py"], check=True)
    # curses.wrapper(fallout_main)
    curses.wrapper(stream_text, t3)
    
    subprocess.run(["python3", "pop-ups.py"], check=True)
    # curses.wrapper(pop_ups_main)
    curses.wrapper(stream_text, t4)
    
    subprocess.run(["python3", "quick.py"], check=True)
    # curses.wrapper(quick_main)
    curses.wrapper(stream_text, t5)
#-------------------------------------------------------------------------------------------------#
# ACT 1 - INTRO SEQUENCE                                                                          #
#-------------------------------------------------------------------------------------------------#
def act1(stdscr):
    height, width = stdscr.getmaxyx()

    username = enter_name(stdscr)
    USERNAME = username

    computer_texts = [
        f">>> Welcome, Operative. Code name: {username}",
        ">>> Mission: Heist Protocol - Operation Monaco",
        ">>> Objective: Hack into Quantum Financials Trust servers",
        "    and wire 40 million to offshore account [3141-5926-5358].",
        "",
        "Press [SPACE] to continue."
    ] 
    display_computer_text(stdscr, computer_texts)
    key = stdscr.getch()
    
    stdscr.clear()
    computer_texts2 = [
        ">>> Initiating connection to Server...",
        ">>> Establishing secure link...",
        "",
        ">>> Access granted."
    ] 
    display_computer_text(stdscr, computer_texts2, blinking=True)
    key = stdscr.getch()
    
    r1 = [
        (f'{username}! {username}! What the fuck are you doing?!', 'Roadman'),
        ("You're in, this is the only chance we got.", 'Roadman'),
        ("We're monitoring your progress from HQ. No mistakes.", 'Roadman'),
        ('@Bla3kH4wk and @AlexeiX, you two access the financial records.', 'Roadman'),
        (f'{username}, press [SPACE] to begin the transfer protocol.', 'Roadman')
    ]
    stream_text(stdscr, r1)
    stdscr.clear()
    
    computer_texts3 = [
        ">>> Accessing financial records...",
        "",
        ">>> Access granted.",
        ">>> Connecting to offshore account..."
    ] 
    display_computer_text(stdscr, computer_texts3)
    
    # TODO: fix this or make it more user friendly
    account_number = "314159265358"  # Example account number
    if enter_account_number(stdscr, account_number):
        stdscr.clear()
        final_texts = [
            ">>> Account number verified.",
            ">>> Transfer in progress..."
        ]
        display_computer_text(stdscr, final_texts)
        max_width = 50  # Width of the progress bar
        for progress in range(100):
            if progress >= 99:
                progress = 99  # Stop at 99%
                time.sleep(5)
            display_progress_bar(stdscr, progress, max_width)
            time.sleep(0.05)  # Control the speed of the progress bar
    else:
        stdscr.addstr(0, 0, "Operation aborted.")
        stdscr.refresh()
        time.sleep(2)
    computer_texts3 = [
        ">>> Access DENIED.",
        ">>> Security Breach Detected!",
        "",
        "Press [SPACE] to continue."  
    ] 
    message = "ALERT"
    start_row = 2
    start_col = 10
    stdscr.refresh()
    stdscr.clear()
    print_large_message(stdscr, message, start_row, start_col)
    stdscr.refresh()

    display_computer_text(stdscr, computer_texts3)

    while True:
        key = stdscr.getch()
        if key == ord(' '):
            break
    
    r2 = [
        ("They've bugged the account.", 'Roadman'),
        (f'{username} you need to disable security. NOW.', 'Roadman')
    ]
    stdscr.refresh()
    stdscr.clear()
    stream_text(stdscr, r2)
    
    # IMPOSSIBLE TYPING PUZZLE
    stdscr.refresh()
    stdscr.clear()
    typing_puzzle(stdscr)
    
    computer_texts4 = [
        ">>> Countermeasures engaged. Shutting down Connection."
    ] 
    stdscr.refresh()
    stdscr.clear()
    display_computer_text(stdscr, computer_texts4)
    key = stdscr.getch()
    
    r3 = [
        (f"For fucks sake {username}, what's happening. I thought you were supposed to be good.", 'Roadman'),
        ("Abort! Get out of there now! We're cooked.", 'Roadman')
    ]
    stdscr.refresh()
    stdscr.clear()
    stream_text(stdscr, r3)
    
    # TODO: make text red
    computer_texts5 = [
        ">>> INITIATING TROJAN DEFENCE SEQUENCE.",
        ">>> TRACKING SOURCE LOCATION.",
        ">>> TRACE INITIATED."
    ]
    stdscr.refresh()
    stdscr.clear()
    display_computer_text(stdscr, computer_texts5)
    key = stdscr.getch()
    
    r4 = [
        (f"Shit, it's too late. You need to wipe your computer and disappear.", 'Roadman')
    ]
    stdscr.refresh()
    stdscr.clear()
    stream_text(stdscr, r4)
    
    computer_texts6 = [
        ">>> TRACE COMPLETE. LOCATION IDENTIFIED.",
        ">>> DEPLOYING COUNTER-OPS..."
    ]
    stdscr.refresh()
    stdscr.clear()
    display_computer_text(stdscr, computer_texts6)
    key = stdscr.getch()
    
    r5 = [
        (f"They've got us too. We're compromised. Go dark. You’re on your own now.", 'Roadman')
    ]
    stdscr.refresh()
    stdscr.clear()
    stream_text(stdscr, r5)

    matrix_wash(stdscr)
    decay_from_top(stdscr)
    time.sleep(2)
    
    computer_texts7 = [
        ">>> FROM: Unknown",
        ">>> SUBJECT: Consequences.",
        ">>> MESSAGE: ",
        (f">>> {username},"),
        "    Your actions have led to consequences. Things you can't come back",
        "    from. You've been blacklisted from the network. All your accounts",
        "    have been frozen. Trust no one.",
        "    Good luck.",
    ]
    stdscr.refresh()
    stdscr.clear()
    display_computer_text(stdscr, computer_texts7)
    key = stdscr.getch()
    
    computer_texts8 = [
        "[CHECKPOINT REACHED]"
    ]
    stdscr.refresh()
    stdscr.clear()
    display_computer_text(stdscr, computer_texts8)
    key = stdscr.getch()
    while True:
        key = stdscr.getch()
        if key == ' ':
            break
    

def act2(stdscr):
    username = USERNAME
    # TODO: make text red
    computer_texts1 = [
        "***this is act 2***"
    ]
    stdscr.refresh()
    stdscr.clear()
    display_computer_text(stdscr, computer_texts1)
    
    



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

    # SET TO 'True' TO SEE DEVELOPMENT STORY
    realstory = True

    # Execute the selected option
    if selected_idx == 0:
        matrix_wash(stdscr)
        decay_from_top(stdscr)
        if realstory:
            act1(stdscr)
            act2(stdscr)
        else:
            username = enter_name(stdscr)
            new_ui(username)
    elif selected_idx == 1:
        pass

if __name__ == "__main__":
    curses.wrapper(main)
