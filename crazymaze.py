import curses
import sys
import time

maze = [
    "                                                                       ",
    "   +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+    ",
    "   |        |        |                                            |    ",
    "   +  +--+  +  +--+--+  +--+--+--+--+--+--+--+--+--+  +--+--+--+  +    ",
    "   |     |     |        |     |     |              |     |        |    ",
    "   +--+  +  +--+  +--+--+  +  +  +  +  +--+--+--+  +--+  +  +--+--+    ",
    "   |     |  |     |        |     |  |        |  |  |     |     |  |    ",
    "   +  +--+  +  +--+  +--+--+--+--+--+--+  +--+--+  +--+--+--+  +--+    ",
    "   |  |     |  |  |  |              |  |  |     |        |  |     |    ",
    "   +  +--+--+  +--+  +  +--+--+--+  +  +  +  +  +--+  +  +--+--+  +    ",
    "   |        |  |     |     |     |  |  |     |     |  |           |    ",
    "   +  +--+  +  +  +--+--+  +--+  +  +--+--+--+--+  +  +--+--+--+--+    ",
    "   |  |     |  |        |     |  |              |  |           |  |    ",
    "   +  +  +--+  +--+--+--+--+  +  +--+--+--+--+  +  +--+  +--+  +--+    ",
    "   |  |  |                    |              |  |     |  |  |     |    ",
    "   +  +  +  +--+--+--+--+--+--+--+  +--+--+  +- +--+  +  +  +--+  +    ",
    "   |  |        |     |                    |  |     |  |     |     |    ",
    "   +  +--+--+  +  +  +  +--+  +--+--+  +--+--+  +  +  +--+  +  +--+    ",
    "   |  |        |  |  |     |        |  |        |  |  |  |  |     |    ",
    "   +  +  +--+--+  +  +--+  +  +--+--+--+  +--+--+--+--+  +  +--+  +    ",
    "   |  |  |        |     |  |     |     |           |  |     |  |  |    ",
    "   +  +  +  +--+--+--+--+  +--+  +  +--+--+--+--+  +  +--+--+--+  +    ",
    "   |  |                       |  |     |  |  |     |        |  |  |    ",
    "   +  +  +--+--+--+--+--+--+--+--+--+  +--+--+  +--+--+--+  +--+  +    ",
    "   |  |        |     |  |        |  |  |  |              |  |     |    ",
    "   +--+--+--+  +  +  +  +  +--+  +--+  +--+  +--+  +--+--+  +  +--+    ",
    "   |     |     |  |  |  |  |  |        |  |  |     |     |  |     |    ",
    "   +  +--+  +--+  +  +  +  +--+--+--+--+--+  +  +--+  +  +  +--+--+    ",
    "   |           |  |  |  |                 |  |  |     |  |        |    ",
    "   +--+--+--+  +--+  +  +--+--+--+--+--+  +  +  +--+--+--+--+--+  +    ",
    "                     |                 |     |              |     E    ",
    "   +-----+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+    ",
    "                                                                       "
]

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.keypad(1)    # Enable special Key values
    stdscr.nodelay(1)   # Make getch non-blocking
    curses.noecho()     # Turn off auto-echoing of keypress on to screen
    curses.cbreak()     # React to keys instantly, without waiting for enter to be pressed
    h, w = stdscr.getmaxyx()

    y, x = 30, 1  # Start position
    previous_position = (y, x)

    # Initial drawing of the maze
    for i, row in enumerate(maze):
        stdscr.addstr(i, 0, row)
    stdscr.addstr(y, x, '@')
    stdscr.refresh()

    start_time = time.time()  # Start the timer
    duration = 120  # 2 minutes in seconds
    timer_x = max(len(row) for row in maze) + 5  # Position for the timer

    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    while True:
        remaining_time = max(0, duration - int(time.time() - start_time))
        mins, secs = divmod(remaining_time, 60)
        timer_str = f"Time: {mins:02}:{secs:02}"
        stdscr.addstr(1, timer_x, timer_str)  # Display timer

        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(1, timer_x, timer_str)
        stdscr.attroff(curses.color_pair(1))

        key = stdscr.getch()
        stdscr.addstr(y, x, ' ')  # Clear the old player position

        # Determine the action based on key press
        if key == curses.KEY_UP and maze[y-1][x] not in ['-', '|', '+']:
            y -= 1
        elif key == curses.KEY_DOWN and maze[y+1][x] not in ['-', '|', '+']:
            y += 1
        elif key == curses.KEY_LEFT and maze[y][x-1] not in ['-', '|', '+', 'S']:
            x -= 1
        elif key == curses.KEY_RIGHT and maze[y][x+1] not in ['-', '|', '+']:
            x += 1
        elif key == ord('q'):  # Quit the game
            break

        # Redraw the player at the new position
        stdscr.addstr(y, x, '@')
        stdscr.refresh()  # Minimize the use of refresh

        # Check if the player has reached the exit
        if maze[y][x] == 'E':
            stdscr.addstr(h//2, w//2 - len("You won!")//2, "You won!")
            stdscr.refresh()
            stdscr.getch()
            break
        
        # Check if time's up
        if remaining_time <= 0:
            stdscr.addstr(h//2, w//2 - len("Time's up!")//2, "Time's up!")
            stdscr.refresh()
            stdscr.getch()
            # this could be sys.exit(100) to exit the program, but for now break
            break
            

if __name__ == "__main__":
    curses.wrapper(main)
