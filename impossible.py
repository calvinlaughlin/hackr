import curses
import random
import time

# List of random codes
codes = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliet", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo", "sierra", "tango", "uniform", "victor", "whiskey", "xray", "yankee"]

def typing_puzzle(stdscr):
    # Setup curses
    curses.curs_set(1)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Initialize variables
    start_time = time.time()
    # timer_duration = 60
    timer_duration = 1 # For testing purposes
    input_text = ""
    code_list = [random.choice(codes) for _ in range(50)]
    current_code = code_list.pop(0)

    while True:
        # Calculate remaining time
        elapsed_time = time.time() - start_time
        remaining_time = max(0, timer_duration - int(elapsed_time))
        
        # Clear screen
        stdscr.clear()

        # Display timer
        stdscr.addstr(0, curses.COLS - 10, f"Time: {remaining_time}s")
        
        # Display upcoming codes and count
        stdscr.addstr(0, 0, f"UPCOMING CODES ({len(code_list)})")
        for idx, code in enumerate(code_list[:10], start=1):
            stdscr.addstr(idx, 0, code)
        
        # Display current code to type
        stdscr.addstr(2, curses.COLS // 2 - len(current_code) // 2, current_code)
        
        # Display input text
        stdscr.addstr(4, curses.COLS // 2 - len(input_text) // 2, input_text)
        
        # Refresh the screen
        stdscr.refresh()
        
        # Get user input
        try:
            key = stdscr.getkey()
        except:
            continue
        
        if key == '\n':
            # Check if input text matches current code
            if input_text == current_code and code_list:
                current_code = code_list.pop(0)
            input_text = ""
        elif key == '\b' or key == '\x7f':  # Handle backspace
            input_text = input_text[:-1]
        elif len(key) == 1:
            input_text += key

        # End the game after the timer runs out
        if remaining_time <= 0:
            break

    # Game over screen
    stdscr.clear()
    stdscr.addstr(curses.LINES // 2, curses.COLS // 2 - 5, "TIME UP!")
    stdscr.refresh()
    time.sleep(2)
