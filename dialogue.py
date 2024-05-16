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