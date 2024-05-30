import curses

# Desired minimum terminal size
MIN_ROWS = 40
MIN_COLS = 140

def check_terminal_size(stdscr):
    curses.curs_set(0)  # Hide the cursor
    while True:
        # Get the current terminal size
        max_y, max_x = stdscr.getmaxyx()

        # Check if the terminal meets the minimum size requirements
        if max_y >= MIN_ROWS and max_x >= MIN_COLS:
            # Clear the screen and display the message to continue
            stdscr.clear()
            msg = "Terminal size is sufficient! Press [SPACE] to continue."
            stdscr.addstr(max_y // 2, (max_x - len(msg)) // 2, msg)
            stdscr.refresh()
            
            # Wait for the user to press SPACE
            while True:
                key = stdscr.getch()
                if key == ord(' '):  # SPACE key
                    return
        else:
            # Display the message to resize the terminal
            stdscr.clear()
            msg = f"Please resize your terminal to at least {MIN_COLS} columns and {MIN_ROWS} rows."
            stdscr.addstr(max_y // 2, (max_x - len(msg)) // 2, msg)
            stdscr.refresh()
        
        # Refresh and wait for a short time before checking again
        stdscr.refresh()
        curses.napms(500)  # Sleep for 500 milliseconds

def main(stdscr):
    # Call the function to check the terminal size
    check_terminal_size(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
