import curses
import random

def draw_matrix(screen):
    # Initialize screen
    curses.curs_set(0)  # Invisible cursor
    screen.nodelay(True)  # Non-blocking input
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    screen.bkgd(' ', curses.color_pair(1))

    # Get initial dimensions
    height, width = screen.getmaxyx()
    column_position = [0] * width

    try:
        while True:
            # Adjust for terminal resizing
            new_height, new_width = screen.getmaxyx()
            if new_height != height or new_width != width:
                height, width = new_height, new_width
                column_position = [0] * width  # Reset positions

            # Update the screen with random characters
            for i in range(width):
                if column_position[i] < height - 1:  # Ensure within screen bounds
                    char = random.choice(['0', '1'])
                    screen.addstr(column_position[i], i, char, curses.color_pair(1))
                    column_position[i] += 1
                if column_position[i] >= height - 1 or random.randint(0, 15) == 0:
                    column_position[i] = 0

            screen.refresh()
            screen.timeout(100)  # Speed of the rain
            if screen.getch() == ord('q'):  # Exit on 'q'
                break
    finally:
        # Clean up and restore terminal
        curses.endwin()

# Run the program
curses.wrapper(draw_matrix)
