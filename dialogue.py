import time
import random
import curses
import pygame

# Initialize Pygame for the entire application lifecycle
pygame.init()
pygame.mixer.init()

# Load a sound (ensure you have a 'text.wav' file in your project directory)
key_sound = pygame.mixer.Sound('text.wav')

def stream_text(stdscr, messages):
    height, width = stdscr.getmaxyx()
    
    for message, character in messages:
        stdscr.clear()  # Clear the screen before starting a new message
        if character:
            label_text = f"{character.upper()}: "
            static_row = height // 2
            label_col = (width - len(message) - len(label_text)) // 2
            stdscr.addstr(static_row, label_col, label_text, curses.A_BOLD)
        else:
            static_row = height // 2
            label_col = (width - len(message)) // 2

        message_col = label_col + len(label_text if character else '')

        stdscr.refresh()  # Refresh after setting up labels and before typing starts

        # Print each character with a sound effect at a random chance
        for i, char in enumerate(message):
            stdscr.addch(static_row + 1, message_col + i, char)  # Place each character
            stdscr.refresh()  # Refresh after each character to see the typing effect
            if random.random() < 0.25:  # Play sound with some probability
                key_sound.play()
            time.sleep(0.03)  # Typing speed

        time.sleep(1)  # Pause after each message
    stdscr.clear()  # Clear the screen after all messages are displayed

def enter_name(stdscr):
    curses.curs_set(1)  # Show the cursor
    curses.echo()  # Enable echoing of characters
    name = ""
    prompt = ">>> USERNAME: "

    intro_text = [
        "Welcome to the hackOS monitor.",
        "Your hackOS connection id is 42",
        "Server version: 1.0.0-hackOS 0ubuntu1",
        "",
        "Copyright (c) 2024, hackOS Corporation.",
        "",
    ]

    stdscr.clear()
    height, width = stdscr.getmaxyx()

    # Calculate center position for the prompt
    prompt_x = (width - int(len(prompt) * 2.75)) // 2
    input_y = height // 2

    # Calculate start position for intro text halfway between top and username input
    intro_start_y = (input_y // 2) - (len(intro_text) // 2)

    # Display the introductory text
    for i, line in enumerate(intro_text):
        x = (width - len(line)) // 2
        stdscr.addstr(intro_start_y + i, x, line)
        stdscr.refresh()
        time.sleep(0.1)  # Simulate typing effect

    # Display the input prompt for the first time
    stdscr.addstr(input_y, prompt_x, prompt)
    stdscr.refresh()

    while True:
        char = stdscr.getch()

        if char == curses.KEY_ENTER or char in [10, 13]:
            break
        elif char == curses.KEY_BACKSPACE or char == 127:
            if len(name) > 0:
                name = name[:-1]
                stdscr.addstr(input_y, prompt_x + len(prompt) + len(name), ' ')
                stdscr.move(input_y, prompt_x + len(prompt) + len(name))
        elif char == curses.KEY_RESIZE:
            height, width = stdscr.getmaxyx()
            prompt_x = (width - len(prompt)) // 2
            input_y = height // 2
            intro_start_y = (input_y // 2) - (len(intro_text) // 2)
            stdscr.clear()
            for i, line in enumerate(intro_text):
                x = (width - len(line)) // 2
                stdscr.addstr(intro_start_y + i, x, line)
            stdscr.addstr(input_y, prompt_x, prompt + name)
        else:
            name += chr(char)

        # Clear the current input line to avoid artifacts
        stdscr.addstr(input_y, prompt_x + len(prompt), ' ' * (width - prompt_x - len(prompt)))
        
        # Update the input prompt with the current name
        stdscr.addstr(input_y, prompt_x + len(prompt), name)
        stdscr.refresh()

    curses.noecho()  # Disable echoing of characters
    curses.curs_set(0)  # Hide the cursor

    return name.upper()
