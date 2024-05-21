import time
import random
import curses
import pygame

# Initialize Pygame for the entire application lifecycle
pygame.init()
pygame.mixer.init()

large_letters = {
    'A': [
        "  ##  ",
        " #  # ",
        "#    #",
        "######",
        "#    #",
        "#    #"
    ],
    'L': [
        "#     ",
        "#     ",
        "#     ",
        "#     ",
        "#     ",
        "######"
    ],
    'E': [
        "######",
        "#     ",
        "##### ",
        "#     ",
        "#     ",
        "######"
    ],
    'R': [
        "##### ",
        "#    #",
        "##### ",
        "#  #  ",
        "#   # ",
        "#    #"
    ],
    'T': [
        "######",
        "  ##  ",
        "  ##  ",
        "  ##  ",
        "  ##  ",
        "  ##  "
    ],
    ' ': [
        "      ",
        "      ",
        "      ",
        "      ",
        "      ",
        "      "
    ]
}

# Load a sound (ensure you have a 'text.wav' file in your project directory)
key_sound = pygame.mixer.Sound('text.wav')

def stream_text(stdscr, messages):
    height, width = stdscr.getmaxyx()

    for message, character in messages:
        stdscr.clear()  # Clear the screen before starting a new message
        if character:
            label_text = f"{character.upper()}: "
            static_row = height // 2
            label_col = 10
            stdscr.addstr(static_row, label_col, label_text, curses.A_BOLD)
        else:
            static_row = height // 2
            label_col = 10

        message_col = label_col + len(label_text if character else '')

        stdscr.refresh()  # Refresh after setting up labels and before typing starts

        # Print each character with a sound effect at a random chance
        for i, char in enumerate(message):
            stdscr.addch(static_row + 1, message_col + i, char)  # Place each character
            stdscr.refresh()  # Refresh after each character to see the typing effect
            if random.random() < 0.25:  # Play sound with some probability
                key_sound.play()
            time.sleep(0.03)  # Typing speed

        stdscr.addstr(height - 1, 0, "Press SPACE to continue...")  # Prompt user to continue
        stdscr.refresh()
        
        # Wait for the user to press space to continue
        while True:
            key = stdscr.getch()
            if key == ord(' '):  # Check if the space key is pressed
                break

        # time.sleep(1)  # Optional pause after each message


def display_computer_text(stdscr, texts, blinking=False):
    height, width = stdscr.getmaxyx()
    midpoint_y = height // 2
    y = midpoint_y // 2
    x = 10  # 2 spaces padding from the right edge

    stdscr.nodelay(True)  # Make getch non-blocking

    # Simulate typing effect
    for i in range(len(texts)):
        stdscr.addstr(y + i, x, texts[i])
        stdscr.refresh()
        if i != len(texts) - 1:
            time.sleep(1)  # Typing speed
        if i == len(texts) - 1:
            if blinking:
                for _ in range(3):
                    stdscr.addstr(y + i, x, texts[i], curses.A_BLINK | curses.A_BOLD)
                    stdscr.refresh()
                    time.sleep(0.5)
                    stdscr.addstr(y + i, x, " " * len(texts[i]))
                    stdscr.refresh()
                    time.sleep(0.5)
                # Ensure the text is shown at the end without blink
                stdscr.addstr(y + i, x, texts[i], curses.A_BOLD)
                stdscr.refresh()
            else:
                stdscr.addstr(y + i, x, texts[i], curses.A_BOLD)
                stdscr.refresh()
    
    stdscr.nodelay(False)

def enter_name(stdscr):
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

    curses.curs_set(1)  # Show the cursor
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

    stdscr.clear()
    return name.upper()

def display_large_text(stdscr, text, start_row, start_col):
    for row_offset, line in enumerate(text):
        for col_offset, char in enumerate(line):
            stdscr.addch(start_row + row_offset, start_col + col_offset, char)

def print_large_message(stdscr, message, start_row, start_col):
    for char in message:
        if char in large_letters:
            for i, line in enumerate(large_letters[char]):
                stdscr.addstr(start_row + i, start_col, line)
            start_col += len(large_letters[char][0]) + 1  # Move to the next character position
        else:
            start_col += 6  # Arbitrary space for characters not in the dictionary
    stdscr.refresh()

def display_code_like_text(stdscr, text, y, x):
    for char in text:
        stdscr.addstr(y, x, char, curses.A_BOLD)
        stdscr.refresh()
        time.sleep(0.05)
        x += 1

def enter_account_number(stdscr, account_number):
    height, width = stdscr.getmaxyx()
    y = height // 2
    x = width // 2 - len("Enter account number: ") // 2

    prompt = "Enter account number: "
    stdscr.addstr(y, x, prompt, curses.A_BOLD)
    stdscr.addstr(y + 1, x, f"Account number: {account_number}", curses.A_DIM)
    stdscr.refresh()

    input_number = ""
    code_texts = [
        "#include <iostream>",
        "#include <cmath>",
        "using namespace std;",
        "int main() {",
        "    double a = 2.5, b = 3.8;",
        "    double result = pow(a, b) + sqrt(a * b) - log(a + b);",
        "    result += sin(result) * cos(a);",
        "    cout << \"Result: \" << result << endl;",
        "    return 0;",
    ]
    code_index = 0

    while True:
        key = stdscr.getch()
        if key in range(48, 58):  # Number keys
            char = chr(key)
            input_number += char
            stdscr.addstr(y, x + len(prompt) + len(input_number) - 1, char, curses.A_BOLD)
            stdscr.refresh()
            # display_code_like_text(stdscr, code_texts[code_index % len(code_texts)], y + 2 + (code_index % len(code_texts)), 0)
            code_index += 1
        elif key == 10:  # Enter key
            if input_number == account_number:
                break
        elif key in (8, 127):  # Backspace key
            if len(input_number) > 0:
                stdscr.addstr(y, x + len(prompt) + len(input_number) - 1, ' ')
                input_number = input_number[:-1]
                stdscr.move(y, x + len(prompt) + len(input_number))
                stdscr.refresh()

    return True

def display_progress_bar(stdscr, progress, max_width):
    height, width = stdscr.getmaxyx()
    bar_width = int(progress * max_width / 100)
    stdscr.addstr(height // 2 + 2, (width - max_width) // 2, '[' + '#' * bar_width + ' ' * (max_width - bar_width) + ']')
    stdscr.addstr(height // 2 + 3, (width - max_width) // 2, f"Progress: {progress}%")
    stdscr.refresh()

def main(stdscr):
    # Test enter_name function
    username = enter_name(stdscr)
    stdscr.clear()
    stdscr.addstr(0, 0, f"Username entered: {username}")
    stdscr.refresh()
    time.sleep(2)

    # Test display_computer_text function
    stdscr.clear()
    computer_texts = [
        f">>> Welcome, Operative. Code name: {username}",
        ">>> Mission: Heist Protocol – Operation Monaco",
        ">>> Objective: Hack into Quantum Financials Trust servers",
        "    and wire 40 million to offshore account [3141-5926-5358].",
        "",
        "Press [SPACE] to continue."
    ]
    display_computer_text(stdscr, computer_texts)
    key = stdscr.getch()

    # Test enter_account_number function
    account_number = "314159265358"  # Example account number
    stdscr.clear()
    if enter_account_number(stdscr, account_number):
        stdscr.clear()
        final_texts = [
            ">>> Account number verified.",
            ">>> Transfer in progress...",
            ">>> Transfer complete. Mission accomplished."
        ]
        display_computer_text(stdscr, final_texts)
    else:
        stdscr.addstr(0, 0, "Operation aborted.")
        stdscr.refresh()
        time.sleep(2)

if __name__ == "__main__":
    curses.wrapper(main)
    pygame.quit()
