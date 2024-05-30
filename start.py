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
from haystack import hay_main

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
    
    computer_texts2 = [
        ">>> Initiating connection to Server...",
        ">>> Establishing secure link...",
        "",
        ">>> Access granted. [SPACE]"
    ] 
    display_computer_text(stdscr, computer_texts2, blinking=True)

    # prompt user if they would like to call him road or roadman
    
    r1 = [
        (f'{username}! What took you so fucking long?', 'Roadman'),
        ("You're in, this is the only chance we got.", 'Roadman'),
        ("This system is running ArmorSafe v2. It's strong, but its not unbreakable!", 'Roadman'),
        ('@Bla3kH4wk and @AlexeiX, you two access the financial records.', 'Roadman'),
        (f'{username}, press [SPACE] to begin the transfer protocol.', 'Roadman')
    ]
    stream_text(stdscr, r1)
    
    computer_texts3 = [
        ">>> Accessing financial records...",
        "",
        "ERROR: Press [SPACE] to align access ports now."
    ] 
    display_computer_text(stdscr, computer_texts3, autocomplete=False)

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
    # message = "ALERT"
    # start_row = 1
    # start_col = 10
    # stdscr.refresh()
    # stdscr.clear()
    # print_large_message(stdscr, message, start_row, start_col)
    # stdscr.refresh()

    display_computer_text(stdscr, computer_texts3)
    
    r2 = [
        ("Ah, shit. They bugged the account. This is REALLY bad.", 'Roadman'),
        (f'{username}, the only way to avoid getting shut down is by guessing the security question.', 'Roadman'),
        (f"Looks like the question was 'childhood dog name'. I've assembled a list of 50 most common dog names.", 'Roadman'),
        (f"Type 'em in as fast as you can. If the timer expires before you succeed, it's all over.", 'Roadman'),
        (f"We're all counting on you.", 'Roadman')
    ]
    stdscr.refresh()
    stream_text(stdscr, r2)
    
    # IMPOSSIBLE TYPING PUZZLE
    stdscr.refresh()
    stdscr.clear()
    typing_puzzle(stdscr)
    
    computer_texts4 = [
        ">>> Countermeasures engaged. Shutting down Connection.",
        "[SPACE]"
    ] 
    stdscr.refresh()
    display_computer_text(stdscr, computer_texts4)
    
    r3 = [
        (f"For fucks sake {username}, what's happening? I thought you were supposed to be good.", 'Roadman'),
        ("Abort! Get out of there now! We're cooked.", 'Roadman')
    ]
    stdscr.refresh()
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
    display_computer_text(stdscr, computer_texts5)
    
    r4 = [
        (f"Shit, it's too late. You need to wipe your computer and disappear.", 'Roadman')
    ]
    stream_text(stdscr, r4)
    
    computer_texts6 = [
        ">>> TRACE COMPLETE. LOCATION IDENTIFIED.",
        ">>> DEPLOYING COUNTER-OPS...",
        "",
        "Press [SPACE] to continue."
    ]
    display_computer_text(stdscr, computer_texts6)
    
    r5 = [
        (f"You're on your own now, {username}. Lay low. Get the hell outta dodge.", 'Roadman')
    ]
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
    display_computer_text(stdscr, computer_texts7)
    
    computer_texts8 = [
        "[CHECKPOINT REACHED]"
    ]
    display_computer_text(stdscr, computer_texts8)

    # BEGIN ACT 2
    act2(stdscr, username)
    

#-------------------------------------------------------------------------------------------------#
# ACT 2 - CUBA REDEMPTION                                                                         #
#-------------------------------------------------------------------------------------------------#
def act2(stdscr, username):
    # TODO: make text red
    stdscr.clear()
    intro = [
        ">>> Location: Cuba",
        ">>> Date: 08/20/1997",
        ">>> Time: 2221 Hours",
        "",
        ">>> 6 months after OPERATION MONACO",
        "[SPACE]"
    ]
    display_computer_text(stdscr, intro)
    
    hello = [
        f">>> Welcome, Operative. Code name: {username}",
        ">>> Status: Blacklisted",
        ">>> Objective: Survive and Locate Allies",
        "",
        "[SPACE]"
    ]
    display_computer_text(stdscr, hello)

    log1 = [
        ("It’s been 6 months since I’ve been ex-communicated.", "[USER LOG #431]"),
        ("The police have followed me to Cuba! Those fuckers.", "[USER LOG #431]"),
        ("It’s not safe here, I need to find somewhere else.", "[USER LOG #431]"),
        ("I just need access to a secure server to reach the GATEKEEPER.", "[USER LOG #431]"),
        ("Navigating this city feels like a maze, but it’s my only chance.", "[USER LOG #431]")
    ]
    stream_text(stdscr, log1)

    mz1 = [
        f">>> Initiating M.A.Z.E. navigation protocol",
        ">>> Objective: find a safehouse",
        ">>> Avoid surveillance traps and dead ends",
        "[SPACE] to begin protocol"
    ]
    display_computer_text(stdscr, mz1)

    maze_main(stdscr)

    mz1 = [
        ">>> Safe house location CONFIRMED",
        "[SPACE]"
    ]
    display_computer_text(stdscr, mz1)
    
    log2 = [
        ("Whew, ok. I’ve made it to the new safe house.", "[USER LOG #432]"),
        ("It’s a pretty rundown place, barely holding together, but it’ll do for now.", "[USER LOG #432]"),
        ("There’s an incognito server here, looks like it hasn’t been touched in years.", "[USER LOG #432]"),
        ("Great... it’s password protected, just what I needed.", "[USER LOG #432]"),
        ("It looks like I have to crack this terminal to get access.", "[USER LOG #432]"),
        ("I don’t have any room for errors and I only have a few attempts before it locks me out.", "[USER LOG #432]")
    ]
    stream_text(stdscr, log2)

    fall = [
        ">>> Cracking the terminal...",
        ">>> [SPACE] to ENTER PASSWORD CRACK. You have 4 attempts remaining."
    ]
    display_computer_text(stdscr, fall)

    fallout_main(stdscr)

    fall2 = [
        ">>> Password accepted.",
        ">>> ACCESS GRANTED. [SPACE]",
    ]
    display_computer_text(stdscr, fall2, blinking=True)

    log3 = [
        ("Finally, I’m in and I’ve bypassed the old server’s password.", "[USER LOG #433]"),
        ("Now, I can access the Gatekeeper from here.", "[USER LOG #433]"),
        ("It’s my only shot at getting back in the game, but I need to be careful.", "[USER LOG #433]"),
        ("One wrong move, and I could be found out.", "[USER LOG #433]"),
        ("It’s time to reach out and see if I can still pull some strings.", "[USER LOG #433]"),
        ("First, I need to get his IP address.", "[USER LOG #433]")
    ]
    stream_text(stdscr, log3)

    needle = [
        ">>> Network Unreliable. TOR server required.",
        ">>> Initiating Signal Trace Protocol...",
        ">>> [SPACE] to locate the correct IP address. Be cautious of decoys and false leads."
    ]
    display_computer_text(stdscr, needle)

    hay_main(stdscr)

    final = [
        ">>> Signal trace successful.",
        ">>> (1) New message received.",
        "[SPACE] to open mail"
    ]
    display_computer_text(stdscr, final)

    msg = [
        ">>> From: Gatekeeper",
        ">>> SUBJECT: Redemption.",
        ">>> MESSAGE:",
        f"    {username},",
        "    Your fall from grace was severe, but there may be a way back.",
        "    Meet me at the following coordinates. I unfroze one of your accounts,",
        "    codenamed PHOENIX. You should have enough funds there. Trust no one.",
        ">>> COORDINATES: [Encrypted]",
        "[SPACE]"
    ]
    display_computer_text(stdscr, msg)

    chck = [
        "[CHECKPOINT 2 REACHED]",
        "[SPACE] to continue to ACT III"
    ]
    display_computer_text(stdscr, chck)


def main(stdscr):
    # Turn off cursor blinking
    curses.curs_set(0)

    # Color setup
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

    selected_idx = 0
    # options = ["Start", "Options"]
    options = ["Start", "Skip to Act II", "Skip to Act III", "Skip to Act IV", "Options"]

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




    
    matrix_wash(stdscr)
    decay_from_top(stdscr)
    if selected_idx == 0: 
        act1(stdscr)
        act2(stdscr, USERNAME)
    else: 
        username = enter_name(stdscr)
        USERNAME = username

        if selected_idx == 1: 
            act2(stdscr, username)
        

if __name__ == "__main__":
    curses.wrapper(main)
