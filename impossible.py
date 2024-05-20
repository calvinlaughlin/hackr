import time
import random
import curses
import threading
import pygame

# Initialize Pygame for sound effects
pygame.init()
pygame.mixer.init()

# Load a sound (ensure you have a 'text.wav' file in your project directory)
key_sound = pygame.mixer.Sound('text.wav')

def play_sound():
    key_sound.play()

def display_timer(stdscr, start_time):
    height, width = stdscr.getmaxyx()
    y, x = 0, width - 15  # Top-right corner

    while time.time() - start_time < 60:
        elapsed_time = int(time.time() - start_time)
        remaining_time = 60 - elapsed_time
        timer_text = f"Time: {remaining_time}s"
        stdscr.addstr(y, x, timer_text, curses.A_BOLD)
        stdscr.refresh()
        time.sleep(1)

def hacker_puzzle(stdscr):
    height, width = stdscr.getmaxyx()
    start_time = time.time()
    puzzle_instructions = [
        ">>> Initiating decryption protocol...",
        ">>> Decrypt the following codes within 60 seconds!",
        ">>> TYPE FAST OR YOU WILL FAIL!",
        ">>> Press any key to start."
    ]
    
    stdscr.clear()
    for i, line in enumerate(puzzle_instructions):
        stdscr.addstr(height // 2 - 2 + i, (width - len(line)) // 2, line)
        stdscr.refresh()
        time.sleep(1)
    stdscr.getch()

    codes = [
        "42B8AFD9", "7E4A6B13", "3C8E9F2A", "9B5D7C1E",
        "F3A7B8E4", "8C1D9E7B", "E7F3B6C2", "A1B8E9F7"
    ]
    stdscr.clear()

    timer_thread = threading.Thread(target=display_timer, args=(stdscr, start_time))
    timer_thread.start()

    random.shuffle(codes)
    code_index = 0
    user_input = ""
    
    while time.time() - start_time < 60:
        stdscr.clear()
        current_code = codes[code_index % len(codes)]
        stdscr.addstr(height // 2 - 1, (width - len(current_code)) // 2, current_code, curses.A_BOLD)
        stdscr.addstr(height // 2 + 1, (width - len(user_input)) // 2, user_input, curses.A_BOLD)
        stdscr.refresh()
        
        key = stdscr.getch()
        if key == ord(current_code[len(user_input)]):
            user_input += chr(key)
            if random.random() < 0.1:
                play_sound()
            if user_input == current_code:
                code_index += 1
                user_input = ""
        elif key == 27:  # Escape key to exit
            return False
    
    timer_thread.join()

    stdscr.clear()
    stdscr.addstr(height // 2, (width - len(">>> MISSION FAILED! TIME'S UP! <<<")) // 2, ">>> MISSION FAILED! TIME'S UP! <<<", curses.A_BOLD | curses.A_BLINK)
    stdscr.refresh()
    time.sleep(5)
    return True