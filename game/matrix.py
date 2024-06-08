import random
import time
import curses

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