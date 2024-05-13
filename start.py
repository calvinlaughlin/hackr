import curses
import random
import time
import pygame
import subprocess

def matrix_wash(stdscr):
    height, width = stdscr.getmaxyx()
    column_position = [0] * width  # Track the current position in each column

    for _ in range(int(height)):  # Extended rain duration
        for i in range(width):
            if column_position[i] < height - 1:
                char = random.choice(['0', '1'])
                stdscr.addstr(column_position[i], i, char)
                column_position[i] += 1
            if column_position[i] >= height - 1 or random.randint(0, 20) == 0:
                column_position[i] = 0

        stdscr.refresh()
        time.sleep(0.05)

def safe_addstr(stdscr, y, x, char):
    """Safely add a character to the screen with boundary checks."""
    maxy, maxx = stdscr.getmaxyx()
    if y < maxy and x < maxx:  # Ensure the coordinates are within screen bounds
        try:
            stdscr.addstr(y, x, char)
        except curses.error:
            pass  # Ignore errors related to boundary issues

def decay_from_top(stdscr):
    height, width = stdscr.getmaxyx()
    decayed = [[False for _ in range(width)] for _ in range(height)]
    attempts = [[0 for _ in range(width)] for _ in range(height)]

    # message = 'Computer'
    # start_y = height // 2  # Vertical center
    # start_x = (width - len(message)) // 2  # Horizontal center

    while not all(all(row) for row in decayed):  # Check if all characters are decayed
        # stdscr.addstr(start_y, start_x, message, curses.A_BOLD)
        for i in range(width):
            column_decayed = True
            for j in range(height):
                if not decayed[j][i]:
                    if random.randint(0, 20) < 3 + attempts[j][i] // 10:  # Adjust decay probability
                        safe_addstr(stdscr, j, i, ' ')
                        decayed[j][i] = True
                    attempts[j][i] += 1
                    if attempts[j][i] > 50:  # Force decay if too many attempts without success
                        decayed[j][i] = True
                        safe_addstr(stdscr, j, i, ' ')

                if not decayed[j][i]:
                    column_decayed = False

        stdscr.refresh()
        time.sleep(0.05)  # Adjust the speed of decay as needed

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

    

def new_ui():
    messages = [
        ('What took you so fucking long? We don\'t have much time left.  ', 'Reznov'),
        ('Next one\'s all you. Should be simple. You crack it, we\'re in.', 'Reznov'),
        ('Ready? Of course you are. Let\'s finish this job.              ', 'Reznov')
    ]
    curses.wrapper(stream_text, messages)
    curses.endwin()
    
    # Run the maze.py script after the dialogue
    subprocess.run(["python", "maze.py"], check=True)
    subprocess.run(["python", "pop-ups.py"], check=True)


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
        new_ui()
    elif selected_idx == 1:
        show_options()

def start_game():
    print("Starting game...")
    # Implement your game starting logic here

def show_options():
    print("Showing options...")
    # Implement your options logic here

if __name__ == "__main__":
    curses.wrapper(main)
