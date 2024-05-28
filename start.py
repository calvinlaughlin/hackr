import curses
import random
import time
import pygame
import subprocess
from dialogue import stream_text, enter_name, display_computer_text, enter_account_number, display_progress_bar, print_large_message
from matrix import matrix_wash, decay_from_top
from maze import main as maze_main
from quick import bar_game
# from quick import main as quick_main
# from pop_ups import main as pop_ups_main
from fallout import main as fallout_main
from impossible import typing_puzzle

import curses

# GLOBAL VARS
USERNAME = 'ANONYMOUS'

# PUZZLE TEST BED
def new_ui(stdscr, username='ANONYMOUS'):    
    # text for the dialogue
    t1 = [
        (f'{username}, what took you so fucking long? We don’t have much time left.', 'Wolfe'),
        ('I’m in position. I can practically smell that vault from here.', 'Wolfe'),
        ('First thing, though, I need you to chart me a path through these air vents.', 'Wolfe'),  
        ('I’m completely fuckin lost.', 'Wolfe'),
        ('Get in the security panel and find me a way out of this fuckin rat maze.', 'Wolfe')
    ]
    t2 = [
        ('Ok, I’m in position.', 'Wolfe'),
        ('Waiting for a guard to pass under me… (talking to self) yeah you fuckin’ scum get outta here.', 'Wolfe'),
        ('Alright I’m making my through to the server room to disable the cameras for the rest of the team to get in.', 'Wolfe'),
        ('This place is a bloody fortress.', 'Wolfe'),
        ('Shit mate, there’s a keypad here to get into the server room.', 'Wolfe'),
        ('I need you to hack into the keypad to get me in.', 'Wolfe'),
        ('It looks like you’ve only got four tries.', 'Wolfe'),
    ]
    t3 = [
        ('Alright, I’m in. Good shit working through that keypad. Now I’m in the server room.', 'Wolfe'),
        ('Let me just open this laptop…', 'Wolfe'),
        ('Type the password in…', 'Wolfe'),
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
    
    r1 = [
        (f'{username}! What took you so fucking long?', 'Roadman'),
        ("You're in, this is the only chance we got.", 'Roadman'),
        ("This cat is running ArmorSafe v2. It's strong, but its not unbreakable!", 'Roadman'),
        ('@Bla3kH4wk and @AlexeiX, you two access the financial records.', 'Roadman'),
        (f'{username}, press [SPACE] to begin the transfer protocol.', 'Roadman')
    ]
    stream_text(stdscr, r1)
    stdscr.clear()
    
    computer_texts3 = [
        ">>> Accessing financial records...",
        "",
        "ERROR: Please align access ports now."
    ] 
    display_computer_text(stdscr, computer_texts3)

    bar_game(stdscr)

    # max_width = 50  # Width of the progress bar
    # for progress in range(100):
    #     if progress >= 99:
    #         progress = 99  # Stop at 99%
    #         time.sleep(5)
    #     display_progress_bar(stdscr, progress, max_width)
    #     time.sleep(0.05)  # Control the speed of the progress bar
    

    computer_texts3 = [
        ">>> Access DENIED.",
        ">>> Security Breach Detected!",
        "",
        "Press [SPACE] to continue."  
    ] 
    message = "ALERT"
    start_row = 1
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
        ("Ah, shit. They bugged the account. This is REALLY bad.", 'Roadman'),
        (f'{username}, the only way to avoid getting shut down is by guessing the security question.', 'Roadman'),
        (f"Looks like the question was 'childhood dog name'. I've assembled a list of 50 most common dog names.", 'Roadman'),
        (f"Type 'em in as fast as you can. If the timer expires before you succeed, it's all over.", 'Roadman'),
        (f"We're all counting on you.", 'Roadman')
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
        (f"For fucks sake {username}, what's happening?! I thought you were supposed to be good.", 'Roadman'),
        ("Abort! Get out of there NOW!", 'Roadman')
    ]
    stdscr.refresh()
    stdscr.clear()
    stream_text(stdscr, r3)
    
    # TODO: make text red
    computer_texts5 = [
        ">>> INITIATING TROJAN DEFENCE SEQUENCE.",
        ">>> TRACKING SOURCE LOCATION.",
        ">>> TRACE INITIATED.",
        "",
        "Press [SPACE] to continue."
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
        ">>> DEPLOYING COUNTER-OPS...",
        "",
        "Press [SPACE] to continue."
    ]
    stdscr.refresh()
    stdscr.clear()
    display_computer_text(stdscr, computer_texts6)
    key = stdscr.getch()
    
    r5 = [
        (f"You're on your own now, {username}. Lay low. Get the hell outta dodge.", 'Roadman')
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
        "    You have long been an esteemed member of our organization. However,",
        "    after your actions in Operation Monaco, we are forced to officially",
        "    cut our ties with you. Your accounts have been frozen and your membership",
        "    is revoked. We suggest you disappear. Now.",
        "    Thank you for your contributions. Goodbye.",
        "    [SPACE]"
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

    # BEGIN ACT 2
    act2(stdscr, username)
    

def act2(stdscr, username):
    # TODO: make text red
    intro = [
        ">>> Location: Cuba",
        ">>> Date: 08/20/1997",
        ">>> Time: 2221 Hours",
        "",
        ">>> 6 months after OPERATION MONACO",
        "[SPACE]"
    ]
    display_computer_text(stdscr, intro)
    key = stdscr.getch()

    hello = [
        f">>> Welcome, Operative. Code name: {username}",
        ">>> Status: Blacklisted",
        ">>> Objective: Survive and Locate Allies",
        "",
        "[SPACE]"
    ]
    display_computer_text(stdscr, hello)
    key = stdscr.getch()

    log1 = [
        ("#431: I can't keep operating on this server. If I want to continue hacking, I need a new one.", "[USER LOG]"),
        ("I just have to find one.", "[USER LOG]"),
        ("Hoping to finally contact the GATEKEEPER once I'm running again.", "[USER LOG]"),
        ("Going to attempt a server search. It's the only way.", "[USER LOG]")
    ]
    stream_text(stdscr, log1)

    mz1 = [
        f">>> Initiating M.A.Z.E. protocol",
        ">>> Avoid surveillance traps and dead ends",
        "[SPACE] to begin protocol"
    ]
    display_computer_text(stdscr, mz1)
    key = stdscr.getch()

    maze_main(stdscr)

    mz1 = [
        ">>> SECURE SERVER OBTAINED.",
        ">>> Encryption: SHA-256"
    ]
    display_computer_text(stdscr, mz1)
    key = stdscr.getch()
    
    log2 = [
        ("#432: Found an open server on the dark web. Only problem is it's still encrypted.", "[USER LOG]"),
        ("What's worse, my computer is beat up, barely holding together, but it'll have to do.", "[USER LOG]"),
        ("Going to have to crack it if I want to use it.", "[USER LOG]"),
        ("No room for errors, either. If I fail, I have to keep looking for another opening.", "[USER LOG]"),
        ("Here goes nothing.", "[USER LOG]")
    ]
    stream_text(stdscr, log2)

    fall = [
        ">>> Cracking the terminal...",
        ">>> ENTER PASSWORD. You have 4 attempts remaining."
    ]
    display_computer_text(stdscr, fall)
    key = stdscr.getch()

    fallout_main(stdscr)

    fall2 = [
        ">>> Password accepted.",
        ">>> ACCESS GRANTED."
    ]
    display_computer_text(stdscr, fall2, blinking=True)
    key = stdscr.getch()

    log3 = [
        ("#433: Fuck yeah. I'm in.", "[USER LOG]"),
        ("I'm confident I can access the GATEKEEPER from here", "[USER LOG]"),
        ("Going to have to crack it if I want to use it.", "[USER LOG]"),
        ("No room for errors, either. If I fail, I have to keep looking for another opening.", "[USER LOG]"),
        ("Here goes nothing.", "[USER LOG]")
    ]
    stream_text(stdscr, log3)



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
