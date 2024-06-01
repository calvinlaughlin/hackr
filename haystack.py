import curses
import random
import time
import threading

def initialize_screen():
    stdscr = curses.initscr()
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(True)
    return stdscr

def generate_random_number_pair():
    return f"{random.randint(0, 99):02}"

def generate_random_ip():
    return f"{generate_random_number_pair()}.{generate_random_number_pair()}.{generate_random_number_pair()}.{generate_random_number_pair()}"

def create_grid(rows, cols, target_ip):
    grid = []
    target_position = (random.randint(0, rows - 1), random.randint(0, cols - 4))
    for r in range(rows):
        row = []
        for c in range(cols):
            if (r, c) == target_position:
                row.extend(target_ip.split('.'))
            elif len(row) < cols:
                row.append(generate_random_number_pair())
        while len(row) < cols:  # Ensure row length is exactly 'cols'
            row.append(generate_random_number_pair())
        grid.append(row)
    return grid, target_position

def display_header(stdscr, target_ip):
    header_y = 2
    header_x = (curses.COLS - len("CONNECTING TO THE HOST")) // 2
    stdscr.addstr(header_y, header_x, "CONNECTING TO THE HOST", curses.A_BOLD)
    
    subheader_x = (curses.COLS - len("Compromising global security one IP at a time")) // 2
    stdscr.addstr(header_y + 1, subheader_x, "Compromising global security one IP at a time", curses.A_DIM)
    
    target_ip_x = (curses.COLS - len(target_ip)) // 2
    stdscr.addstr(header_y + 2, target_ip_x, target_ip, curses.A_BOLD | curses.A_BLINK)

def display_grid(stdscr, grid, cursor_pos, highlight=False, success=False):
    start_y = 11
    start_x = (curses.COLS - 3 * len(grid[0])) // 2
    for r, row in enumerate(grid):
        for c, num in enumerate(row):
            x = start_x + c * 3
            y = start_y + r
            if r == cursor_pos[0] and c >= cursor_pos[1] and c < cursor_pos[1] + 4:
                attr = curses.color_pair(2) if not success else curses.color_pair(1)
                if highlight:
                    attr |= curses.A_BLINK
                stdscr.addstr(y, x, num, attr)
            else:
                stdscr.addstr(y, x, num)
    stdscr.refresh()

def display_timer(stdscr, time_left):
    timer_y = 6
    timer_x = (curses.COLS - len("01:00")) // 2
    stdscr.addstr(timer_y, timer_x, f"{int(time_left // 60):02}:{int(time_left % 60):02}", curses.A_BOLD | curses.color_pair(1))
    stdscr.refresh()

def draw_progress_bar(stdscr, progress, max_progress, x, y, width):
    bar_length = int((progress / max_progress) * width)
    stdscr.addstr(y, x, "[" + "#" * bar_length + "-" * (width - bar_length) + "]", curses.color_pair(1))
    stdscr.refresh()

def draw_hacker_art(stdscr):
    art = [
        "  _____             _ _           _   ",
        " |  |  |___ ___ ___| |_|___ ___ _| |_ ",
        " |  |  | . |  _| . | | |   | .'| . |  ",
        " |_____|___|_| |  _|_|_|_|_|__,|___|  ",
        "               |_|                    "
    ]
    start_x = (curses.COLS - max(len(line) for line in art)) // 2
    start_y = 0
    for i, line in enumerate(art):
        stdscr.addstr(start_y + i, start_x, line, curses.color_pair(3))
    stdscr.refresh()

def endgame_message(stdscr, message, color_pair):
    stdscr.clear()
    stdscr.refresh()
    message_x = (curses.COLS - len(message)) // 2
    message_y = curses.LINES // 2
    stdscr.addstr(message_y, message_x, message, curses.A_BOLD | curses.color_pair(color_pair))
    stdscr.refresh()

def hay_main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)

    target_ip = generate_random_ip()  # Randomized target IP
    rows, cols = 10, 30  # Fixed 30x10 grid
    grid, target_position = create_grid(rows, cols, target_ip)
    cursor_pos = [0, 0]

    start_time = time.time()
    time_limit = 60  # Increased time limit to 60 seconds
    end_time = start_time + time_limit
    time_left = time_limit
    timer_running = True

    def update_timer():
        nonlocal time_left, timer_running
        while time_left > 0 and timer_running:
            time_left = max(0, end_time - time.time())
            display_timer(stdscr, time_left)
            draw_progress_bar(stdscr, time_limit - time_left, time_limit, (curses.COLS - 40) // 2, 8, 40)
            time.sleep(0.1)
        if time_left <= 0 and timer_running:
            endgame_message(stdscr, "Times Up! Lost the connection", 2)

    timer_thread = threading.Thread(target=update_timer)
    timer_thread.start()

    stdscr.clear()
    draw_hacker_art(stdscr)
    display_header(stdscr, target_ip)
    display_grid(stdscr, grid, tuple(cursor_pos))
    stdscr.refresh()

    while time_left > 0 and timer_running:
        key = stdscr.getch()

        if key == curses.KEY_UP and cursor_pos[0] > 0:
            cursor_pos[0] -= 1
        elif key == curses.KEY_DOWN and cursor_pos[0] < rows - 1:
            cursor_pos[0] += 1
        elif key == curses.KEY_LEFT and cursor_pos[1] > 0:
            cursor_pos[1] -= 1
        elif key == curses.KEY_RIGHT and cursor_pos[1] < cols - 4:
            cursor_pos[1] += 1
        elif key == ord('q'):
            timer_running = False
            break
        elif key == ord('\n'):
            if tuple(cursor_pos) == target_position:
                timer_running = False
                for _ in range(3):
                    stdscr.clear()
                    draw_hacker_art(stdscr)
                    display_grid(stdscr, grid, tuple(cursor_pos), highlight=True, success=True)
                    stdscr.refresh()
                    time.sleep(0.5)
                    stdscr.clear()
                    draw_hacker_art(stdscr)
                    display_grid(stdscr, grid, tuple(cursor_pos), highlight=False, success=True)
                    stdscr.refresh()
                    time.sleep(0.5)
                endgame_message(stdscr, "Connection Acquired", 1)
                break

        stdscr.clear()
        draw_hacker_art(stdscr)
        display_header(stdscr, target_ip)
        display_grid(stdscr, grid, tuple(cursor_pos))
        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(hay_main)
