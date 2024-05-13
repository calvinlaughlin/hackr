import curses
import time
import pygame
import random

def main(stdscr):
    # Initialize pygame mixer
    pygame.init()
    pygame.mixer.init()

    # Load a sound (ensure you have a 'typewriter-key.wav' file in your project directory)
    key_sound = pygame.mixer.Sound('text.wav')

    def stream_text(message, character='None'):
        if character != 'None':
            static_text = f"{character.upper()}:"
            static_row = 9
            static_col = 10
            stdscr.addstr(static_row, static_col, static_text)

        row = 10
        col = 10

        for char in message:
            stdscr.addch(row, col, char)
            stdscr.refresh()
            # Play the typing sound
            if random.randint(0, len(message) // 4) == 0:  # Adjust the list to change probability
                key_sound.play()
            time.sleep(0.03)  # Adjust as necessary for your typing speed and sound effect duration
            col += 1

    stdscr.clear()
    stream_text('This is a method to stream text. Do with it what you will.', 'Computer')
    stdscr.getch()

curses.wrapper(main)
