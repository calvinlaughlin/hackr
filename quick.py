import curses
import time
import random

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    levels = 10
    start = 0.05
    speeds = [start / (2 ** i) for i in range(levels)]
    positions = [0] * levels
    directions = [1] * levels
    targets = [random.randint(5, 24) for _ in range(levels)]
    padding = 1  # Adding padding to make hitting the target easier
    current_level = 0

    while current_level < levels:
        stdscr.clear()

        for i in range(levels):
            if i == current_level:
                stdscr.addstr(i, 0, "#" + "-" * positions[i] + "|" + "-" * (29 - positions[i] - 1) + "#")
                stdscr.addstr(i, targets[i], "X")
            else:
                stdscr.addstr(i, 0, "#" + "-" * 14 + "|" + "-" * 14 + "#")
                stdscr.addstr(i, targets[i], "X")

        stdscr.refresh()

        key = stdscr.getch()
        if key == ord(' '):
            if targets[current_level] - padding <= positions[current_level] <= targets[current_level] + padding:
                current_level += 1
                if current_level < levels:
                    curses.flash()
                else:
                    break
            else:
                stdscr.addstr(levels, 0, "Game Over! Press any key to exit.")
                stdscr.refresh()
                stdscr.getch()
                return

        time.sleep(speeds[current_level])

        positions[current_level] += directions[current_level]
        if positions[current_level] == 28 or positions[current_level] == 0:
            directions[current_level] *= -1

    stdscr.addstr(levels, 0, "You Win! Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
