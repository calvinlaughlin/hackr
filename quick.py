import curses
import time
import random

def bar_game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    levels = 10
    start = 0.01
    num_tries = 0

    while True:
        speeds = [start / (2 ** i) for i in range(levels)]
        positions = [0] * levels
        directions = [1] * levels
        targets = [random.randint(5, 24) for _ in range(levels)]
        padding = 1  # Adding padding to make hitting the target easier
        current_level = 0

        while current_level < levels:
            # Calculate the starting position for the top right quadrant of the screen
            height, width = stdscr.getmaxyx()
            start_row = (height // 4) - (levels // 2)
            start_col_levels = (width // 2) + (width // 4) - 15  # Adjusted for levels
            start_col_progress = (width // 2) + (width // 4) - 25  # Keep original position for progress bar

            # Clear only the right half of the screen where the game is drawn
            for row in range(start_row, start_row + levels + 4):
                stdscr.move(row, start_col_progress)
                stdscr.clrtoeol()

            for i in range(levels):
                row = start_row + i
                if i == current_level:
                    stdscr.addstr(row, start_col_levels, "#" + "-" * positions[i] + "|" + "-" * (29 - positions[i] - 1) + "#")
                    stdscr.addstr(row, start_col_levels + targets[i], "X")
                else:
                    stdscr.addstr(row, start_col_levels, "#" + "-" * 15 + "-" * 14 + "#")
                    stdscr.addstr(row, start_col_levels + targets[i], "X")

            # Calculate and draw the progress bar
            progress = int((current_level / levels) * 30)
            percentage = int((current_level / levels) * 100)
            progress_bar = "Progress: [" + "#" * progress + "-" * (30 - progress) + "] " + f"{percentage}%"
            stdscr.addstr(start_row + levels + 1, start_col_progress, progress_bar)

            stdscr.refresh()

            key = stdscr.getch()
            if key == ord(' '):
                if targets[current_level] - padding <= positions[current_level] <= targets[current_level] + padding:
                    current_level += 1
                    if current_level < levels:
                        curses.flash()
                    else:
                        # Ensure progress bar reaches 100% before displaying the final message
                        progress_bar = "Progress: [" + "#" * 30 + "] 100%"
                        stdscr.addstr(start_row + levels + 1, start_col_progress, progress_bar)
                        stdscr.refresh()
                        break
                else:
                    break

            time.sleep(speeds[current_level])

            positions[current_level] += directions[current_level]
            if positions[current_level] == 28 or positions[current_level] == 0:
                directions[current_level] *= -1

        if current_level == levels:
            stdscr.addstr(start_row + levels + 2, start_col_progress, "CONNECTED! Press SPACE to transfer ALL FUNDS. ")
            stdscr.addstr(start_row + levels + 3, start_col_progress, "Current balance: $40,203,679,829.72")
            stdscr.refresh()
            while True:
                key = stdscr.getch()
                if key == ord(' '):
                    break
            # Clear only the right half of the screen where the game is drawn
            for row in range(start_row, start_row + levels + 4):
                stdscr.move(row, start_col_progress)
                stdscr.clrtoeol()
            return
        else:
            num_tries += 1
            stdscr.addstr(start_row + levels + 2, start_col_progress, f"Press SPACE to try again. Tries: {num_tries}")
            stdscr.refresh()
            while True:
                key = stdscr.getch()
                if key == ord(' '):
                    break

if __name__ == "__main__":
    curses.wrapper(bar_game)
