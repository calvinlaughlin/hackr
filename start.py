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
from windowsizing import check_terminal_size
from flow import flow_main

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
        ">>> Use the arrow keys to navigate the @ from S to E",
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
        ">>> Use the arrow keys and press enter to guess a word",
        ">>> After each guess, you will be told the number of character slots that it shares with the password",
        ">>> Hint...think wordle.",
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

#-------------------------------------------------------------------------------------------------#
# ACT 3 - THE SET UP                                                                              #
#-------------------------------------------------------------------------------------------------#
def act3(stdscr, username):
    
    stdscr.clear()
    intro = [
        f">>> Location: Perth, Australia", 
        f">>> Date: 11/07/1997",
        f">>> Time: 1400 Hours",
        f"",
        f">>> 9 months after Operation Monaco",
        f"",
        f">>> Press [Space] to continue",
    ]
    display_computer_text(stdscr, intro)

    hello = [
        f">>> Welcome, Operative. Code name:{username}",
        f">>> Status: Ghost",
        f">>> Objective: Prepare and Plan",
        f"",
        f">>> Press [Space] to continue",
    ]
    display_computer_text(stdscr, hello)
    
    log1 = [
        (f"467: Three months since I left Cuba. ", "[USER LOG]"),
        (f"Three months of laying low, slowly crawling my way back into the game. ", "[USER LOG]"),
        (f"I met the Gatekeeper, as planned. ", "[USER LOG]"),
        (f"They’re giving me another shot, but it comes with strings attached. ", "[USER LOG]"),
        (f"Pre-heist jobs, grunt work to set up the big one. ", "[USER LOG]"),
        (f"I've been setting up contacts, gathering intel, and testing systems. ", "[USER LOG]"),
        (f"Each step brings me closer to redemption. ", "[USER LOG]"),
        (f"Now, I'm in Perth. ", "[USER LOG]"),
        (f"The heat from the cops has cooled, but I'm still a ghost. ", "[USER LOG]"),
        (f"The objective is clear: prepare and plan. ", "[USER LOG]"),
        (f"Today, it's about installing new incognito software. ", "[USER LOG]"),
        (f"The Gatekeeper's connections depend on it. ", "[USER LOG]"),
        (f"Can't afford any digital footprints.", "[USER LOG]"),
    ]
    stream_text(stdscr, log1)
    
    pop1 = [
        f">>> Install new Incognito Software.",
        f">>> ERROR: Trojan Horse Detected.",
        f">>> Prevent from being Hacked and Bugged. ",
        f"",
        f">>> Press [Space] to continue",
    ]
    display_computer_text(stdscr, pop1)
    
    # POP UP PUZZLE
    # subprocess.run(["python3", "pop-ups.py"], check=True)
    
    pop2 = [
        f">>> Virus successfully removed. ",
        f">>> Incognito Software Installed.",
        f"",
        f">>> Press [Space] to continue",
    ]
    display_computer_text(stdscr, pop2, blinking=True)
    
    log2 = [
        (f"468: Whew, that was a close one. ", "[USER LOG]"),
        (f"I can’t afford to mess up like that again, but the new incognito software is up and running. ", "[USER LOG]"),
        (f"Now comes the real test. ", "[USER LOG]"),
        (f"The Gatekeeper needs more proof that I can handle the pressure. ", "[USER LOG]"),
        (f"It's time to rewire the network and regain full functionality. ", "[USER LOG]"),
        (f"It’s just like old times, back in Vegas. ", "[USER LOG]"),
        (f"That’s where the real fun happened. ", "[USER LOG]"),
    ]
    stream_text(stdscr, log2)
    
    flow1 = [
        f">>> Patching into network.",
        f">>> Connect the junctions and regain functionality.  ",
        f"",
        f">>> Press [Space] to continue",
    ]
    display_computer_text(stdscr, flow1)
    
    # FLOW PUZZLE
    flow_main(stdscr)
        
    flow2 = [
        f">>> Network functionality restored. ",
        f"",
        f">>> Press [Space] to continue",
    ]
    display_computer_text(stdscr, flow2)
    
    log3 = [
        (f"The network's back online, but it's not over yet. ", "[USER LOG]"),
        (f"The Gatekeeper wants to see speed and precision. ", "[USER LOG]"),
        (f"It's not just about getting back into the game; it's about proving I still have what it takes.", "[USER LOG]"),
        (f"Who knows what will happen if I fuck up. ", "[USER LOG]"),
        (f"I have to lock in. ", "[USER LOG]"),
    ]
    stream_text(stdscr, log3)
    
    quick1 = [
        f">>> >>> Agility test initiated... ",
        f"",
        f">>> Press [Space] to continue",
    ]
    display_computer_text(stdscr, quick1)
    
    # QUICK PUZZLE AGILITY TEST
    subprocess.run(["python3", "quick.py"], check=True)
    
    quick2 = [
        f">>> From: Gatekeeper",
        f">>> SUBJECT: Judgement Day.",
        f">>> MESSAGE:",
        f">>> {username},",
        f">>> You've shown you can still be useful. ",
        f">>> The network is secure, and your skills are where they need to be. ",
        f">>> The real heist is imminent. ",
        f">>> Stay hidden and vigilant. ",
        f">>> I'll send the details when it's time. ",
        f">>> I'll be watching.",
        f">>> Trust no one.",
        f"",
        f">>> Press [Space] to continue",
    ]
    display_computer_text(stdscr, quick2)
    
    computer_texts8 = [
        "[CHECKPOINT REACHED]",
        "[SPACE]"
    ]
    display_computer_text(stdscr, computer_texts8)

#-------------------------------------------------------------------------------------------------#
# ACT 4 - ????????????????                                                                        #
#-------------------------------------------------------------------------------------------------#
def act4(stdscr, username):
    stdscr.clear()
    intro = [
        f">>> Location: [REDACTED]", 
        f">>> Date: 12/25/1997",
        f">>> Time: 0246 Hours",
        f">>> Operation Silent Night",
        f"[SPACE]"
    ]
    display_computer_text(stdscr, intro)

    intro2 = [
        f">>> Welcome, Operative. Code name:{username}", 
        f">>> Status: Active",
        f">>> Objective: Don’t fuck up.",
        f"[SPACE]"
    ]
    display_computer_text(stdscr, intro2)

    road = [
        (f"Hey {username}, remember me?", "Roadman"),
        (f"I can’t afford to mess up like that again, but the new incognito software is up and running. ", "[USER LOG]"),
        (f"Of course you do. Let’s hope this time you’ve got your head on straight.", "Roadman"),
        (f"I swear, if you fuck this up… ", "Roadman"),
    ]
    stream_text(stdscr, road)

    intro3 = [
        f">>> Press [SPACE] to initiate the connection."
    ]
    display_computer_text(stdscr, intro3)

    intro4 = [
        ">>> Initiating connection to Server....",
        ">>> Establishing secure link...",
        ">>> Access granted. [SPACE]"
    ]
    display_computer_text(stdscr, intro3, blinking=True)

    road2 = [
        (f"Just like we rehearsed.", "Roadman"),
        (f"Copa and Zee, access the financial records.", "Roadman"),
        (f"{username}, you need to get us past the firewall.", "Roadman"),
        (f"Do whatever it takes this time.", "Roadman"),
    ]
    stream_text(stdscr, road2)

    cip = [
        ">>> Accessing financial records...",
        ">>> Access granted.",
        ">>> Connecting to offshore account...",
        "",
        "[SPACE] to initiate Firewall Bypass Portal..."
    ]
    display_computer_text(stdscr, cip)

    # INSERT CIPHER PUZZLE HERE

    cip2 = [
        ">>> Firewall penetration 25% complete...",
        ">>> Firewall penetration 50% complete...",
        ">>> Firewall penetration 75% complete...",
        ">>> Firewall penetration 100% complete.",
        ">>> Access to mainframe granted. [SPACE]"
    ]
    display_computer_text(stdscr, cip2)

    road3 = [
        (f"Alright, {username}, not bad.", "Roadman"),
        (f"Bla3kH4wk and AlexeiX. I need you to start covering up our tracks and watch the chatter on the line.", "Roadman"),
        (f"Alert me in case of anything.", "Roadman"),
        (f"{username}, it’s time to connect the accounts.", "Roadman"),
        (f"Remember, wire 90 million to offshore accounts [2352-6837-6469].", "Roadman"),
        (f"You only have about 2 minutes to do this. Be fast.", "Roadman")
    ]
    stream_text(stdscr, road3)

    flw = [
        ">>> Initiating Account Link Protocol…",
        ">>> Connect the two accounts by routing the transfer through secure nodes.",
        ">>> Avoid detection and traps. [SPACE]",
    ]
    display_computer_text(stdscr, flw)

    # INSERT FLOW PUZZLE HERE

    flw2 = [
        ">>> Node connection 25% complete...",
        ">>> Node connection 50% complete...",
        ">>> Node connection 75% complete...",
        ">>> Node connection 100% complete...",
        ">>> Bank accounts successfully linked.",
        "Initiate fund transfer with [SPACE]"
    ]
    display_computer_text(stdscr, flw2)

    road4 = [
        (f"We’re almost there. Everything is going according to plan.", "Roadman")
    ]
    stream_text(stdscr, road4)

    deny = [
        ">>> Access denied.",
        "",
        ">>> ALERT! Security Breach Detected!",
        "",
        "[SPACE?]"
    ]
    display_computer_text(stdscr, deny)

    road5 = [
        (f"Shit. Shit. SHIT.", "Roadman"),
        (f"We’ve got noise on the line, we have to move fast.", "Roadman"),
        (f"Security measures are starting to be activated. They know we're here.", "Roadman"),
        (f"[USER], it’s all up to you. DISABLE IT NOW.", "Roadman")
    ]
    stream_text(stdscr, road5)

    # CRAZY FINAL BOSS PUZZLE FUCK YEAH

    accept = [
        ">>> Security disabled. Re-establish connectio with [SPACE]."
    ]
    display_computer_text(stdscr, accept)

    road6 = [
        (f"We’re still running out of time. We have about 15 seconds before they manually lock us out. Finish the job {username}.", "Roadman")
    ]
    stream_text(stdscr, road6)

    # resume transfer


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
        check_terminal_size(stdscr)
        act1(stdscr)
        act2(stdscr, USERNAME)
        act3(stdscr, USERNAME)
        act4(stdscr, USERNAME)

    if selected_idx == 1: 
        check_terminal_size(stdscr)
        username = enter_name(stdscr)
        USERNAME = username
        act2(stdscr, username)
        act3(stdscr, USERNAME)
        act4(stdscr, USERNAME)

    if selected_idx == 2:
        check_terminal_size(stdscr)
        username = enter_name(stdscr)
        USERNAME = username
        act3(stdscr, USERNAME)
        act4(stdscr, USERNAME)

    if selected_idx == 3:
        check_terminal_size(stdscr)
        username = enter_name(stdscr)
        USERNAME = username
        act4(stdscr, USERNAME)
        

if __name__ == "__main__":
    curses.wrapper(main)
