import curses
import signal
import time
import threading
import random

# Define the junctions and their rotations
class KneeJunction:
    rotations = ['┌', '┐', '┘', '└']

    def __init__(self, state=0):
        self.state = state % 4

    def rotate(self):
        self.state = (self.state + 1) % 4

    def __str__(self):
        return KneeJunction.rotations[self.state]

class TJunction:
    rotations = ['┬', '┤', '┴', '├']

    def __init__(self, state=0):
        self.state = state % 4

    def rotate(self):
        self.state = (self.state + 1) % 4

    def __str__(self):
        return TJunction.rotations[self.state]

class StraightJunction:
    rotations = ['│', '─']

    def __init__(self, state=0):
        self.state = state % 2

    def rotate(self):
        self.state = (self.state + 1) % 2

    def __str__(self):
        return StraightJunction.rotations[self.state]

# Define the initial larger board
initial_board = [
    "┌────┬┬─┬──┬───┬───┐",
    "├───┐│└┐│┌─┴──┬┴┬─┬┤",
    "└──┐││┌┘││    │┌┘ ││",
    "┌──┘└┤└─┴┴───┬┘│┌─┘│",
    "├──┬─┴───┐┌──┴─┴┴──┘",
    "└─┐└────┐││┌─┐┌────┐",
    "┌─┴─┬─┐┌┘││└┬┘│┌───┘",
    "├─┬─┴┬┴┴┐│└┬┤ ││┌──┐",
    "└┐│┌─┴┐┌┴┤ │└─┘││┌─┘",
    " └┴┴──┴┴─┴─┴───┴┴┘",
    "┌────┬┬─┬──┬───┬───┐",
    "├───┐│└┐│┌─┴──┬┴┬─┬┤",
    "└──┐││┌┘││    │┌┘ ││",
    "┌──┘└┤└─┴┴───┬┘│┌─┘│",
    "├──┬─┴───┐┌──┴─┴┴──┘",
    "└─┐└────┐││┌─┐┌────┐",
    "┌─┴─┬─┐┌┘││└┬┘│┌───┘",
    "├─┬─┴┬┴┴┐│└┬┤ ││┌──┐",
    "└┐│┌─┴┐┌┴┤ │└─┘││┌─┘",
    " └┴┴──┴┴─┴─┴───┴┴┘",
]

# Convert the initial board into junction objects
def create_board(initial_board):
    board = []
    for line in initial_board:
        row = []
        for char in line:
            if char in KneeJunction.rotations:
                row.append(KneeJunction(KneeJunction.rotations.index(char)))
            elif char in TJunction.rotations:
                row.append(TJunction(TJunction.rotations.index(char)))
            elif char in StraightJunction.rotations:
                row.append(StraightJunction(StraightJunction.rotations.index(char)))
            else:
                row.append(char)
        board.append(row)
    return board

# Randomly rotate 10 non-space places on the grid
def randomly_rotate(board):
    non_space_positions = [(y, x) for y, row in enumerate(board) for x, cell in enumerate(row) if isinstance(cell, (KneeJunction, TJunction, StraightJunction))]
    random_positions = random.sample(non_space_positions, 20)
    for y, x in random_positions:
        rotations = random.randint(1, 4)
        for _ in range(rotations):
            board[y][x].rotate()

def print_pixel_art(stdscr, y, x, color_pair):
    art = [
        "   .,-:::::/ :::::::..   ::::::::::-.   :::         ...       .,-:::::  :::  .   .,:::::::::::::-.  ",
        ",;;-'````'  ;;;;``;;;;  ;;; ;;,   `';, ;;;      .;;;;;;;.  ,;;;'````'  ;;; .;;,.;;;;'''' ;;,   `';,",
        "[[[   [[[[[[/[[[,/[[['  [[[ `[[     [[ [[[     ,[[     \[[,[[[         [[[[[/'   [[cccc  `[[     [[",
        "\"$$c.    \"$$ $$$$$$c    $$$  $$,    $$ $$'     $$$,     $$$$$$        _$$$$,     $$\"\"\"\"   $$,    $$",
        " `Y8bo,,,o88o888b \"88bo,888  888_,o8P'o88oo,.__\"888,_ _,88P`88bo,__,o,\"888\"88o,  888oo,__ 888_,o8P'",
        "   `'YMUP\"YMMMMMM   \"W\" MMM  MMMMP\"`  \"\"\"\"YUMMM  \"YMMMMMP\"   \"YUMMMMMP\"MMM \"MMP\" \"\"\"\"YUMMMMMMMP\"`  ",
    ]
    for i, line in enumerate(art):
        stdscr.addstr(y + i, x, line, curses.color_pair(color_pair))

# Display the board
def display_board(stdscr, board, cursor_x, cursor_y, time_left, flash_color=False, flash_row=None):
    terminal_height, terminal_width = stdscr.getmaxyx()

    board_height = len(board)
    board_width = max(len(row) for row in board)

    vertical_padding = (terminal_height - board_height - 15) // 2  # Additional -15 for pixel art, progress bar, and clock
    horizontal_padding = (terminal_width - board_width) // 2 + 1  # Move grid one position to the right

    # Display pixel art
    color_pair = 1 if time_left % 2 == 0 else 2
    print_pixel_art(stdscr, vertical_padding, (terminal_width - 115) // 2 + 8, color_pair)  # Move art 10 spaces to the right

    # Display clock
    clock_padding = (terminal_width - 5) // 2 + 1
    clock_color = curses.color_pair(1 if time_left % 2 == 0 else 1)  # Flash red continuously
    clock_minutes, clock_seconds = divmod(time_left, 60)
    clock = f"{clock_minutes:02}:{clock_seconds:02}"
    stdscr.addstr(vertical_padding + 9, clock_padding, clock, clock_color)

    # Display progress bar
    progress_bar_length = 30  # Set progress bar length
    filled_length = int(progress_bar_length * time_left / 60)
    progress_bar = '[' + '=' * filled_length + ' ' * (progress_bar_length - filled_length) + ']'
    
    progress_bar_padding = (terminal_width - progress_bar_length) // 2
    stdscr.addstr(vertical_padding + 10, progress_bar_padding, progress_bar, curses.color_pair(2))

    # Display grid
    for y, row in enumerate(board):
        row_color = curses.color_pair(2) if (flash_color and flash_row == y) else curses.color_pair(0)
        stdscr.addstr(vertical_padding + 12 + y, horizontal_padding, ''.join(str(cell) for cell in row), row_color)

    # Display cursor
    stdscr.addstr(vertical_padding + 12 + cursor_y, horizontal_padding + cursor_x, '@', curses.color_pair(3))

    stdscr.refresh()

def display_win_message(stdscr):
    stdscr.clear()
    terminal_height, terminal_width = stdscr.getmaxyx()

    win_message = "You did it!"
    padding_top = (terminal_height - 1) // 2
    padding_left = (terminal_width - len(win_message)) // 2

    stdscr.addstr(padding_top, padding_left, win_message, curses.color_pair(2))
    stdscr.refresh()

def display_end_message(stdscr):
    stdscr.clear()
    terminal_height, terminal_width = stdscr.getmaxyx()

    end_message = "Times Up!"
    padding_top = (terminal_height - 1) // 2
    padding_left = (terminal_width - len(end_message)) // 2

    stdscr.addstr(padding_top, padding_left, end_message, curses.color_pair(1))
    stdscr.refresh()

def countdown_timer(stdscr):
    global time_left, running
    while time_left > 0 and running:
        time.sleep(1)
        time_left -= 1
        if running:  # Only update the display if the game is still running
            display_board(stdscr, board, cursor_x, cursor_y, time_left)
    if time_left == 0:
        running = False
        display_end_message(stdscr)

def check_win_condition():
    global board, initial_board
    return all(str(board[y][x]) == initial_board[y][x] for y in range(len(board)) for x in range(len(board[y])))

def flash_win(stdscr):
    global board, cursor_x, cursor_y, time_left
    for _ in range(3):  # Repeat the flashing 3 times
        for i in range(len(board)):
            display_board(stdscr, board, cursor_x, cursor_y, time_left, flash_color=True, flash_row=i)
            time.sleep(0.05)  # Flash faster
            display_board(stdscr, board, cursor_x, cursor_y, time_left, flash_color=False, flash_row=i)
            time.sleep(0.05)
    display_win_message(stdscr)
    while True:  # Wait until user presses a key to exit
        if stdscr.getch() != -1:
            break

def main(stdscr):
    signal.signal(signal.SIGINT, lambda s, f: exit_game(stdscr))

    global board, cursor_x, cursor_y, time_left, running
    board = create_board(initial_board)
    randomly_rotate(board)
    cursor_x, cursor_y = 0, 0
    time_left = 60
    running = True

    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)

    timer_thread = threading.Thread(target=countdown_timer, args=(stdscr,))
    timer_thread.daemon = True
    timer_thread.start()

    stdscr.nodelay(True)  # Make getch() non-blocking
    stdscr.timeout(100)   # Refresh every 100ms

    try:
        while running:
            display_board(stdscr, board, cursor_x, cursor_y, time_left)
            key = stdscr.getch()

            if key == ord('q'):
                break
            elif key == curses.KEY_UP and cursor_y > 0:
                cursor_y -= 1
            elif key == curses.KEY_DOWN and cursor_y < len(board) - 1:
                cursor_y += 1
            elif key == curses.KEY_LEFT and cursor_x > 0:
                cursor_x -= 1
            elif key == curses.KEY_RIGHT and cursor_x < len(board[0]) - 1:
                cursor_x += 1
            elif key == ord('r'):
                cell = board[cursor_y][cursor_x]
                if isinstance(cell, (KneeJunction, TJunction, StraightJunction)):
                    cell.rotate()
            if check_win_condition():
                running = False
                flash_win(stdscr)

        if time_left == 0:
            display_end_message(stdscr)
            while True:
                if stdscr.getch() != -1:
                    break

    except KeyboardInterrupt:
        pass
    finally:
        exit_game(stdscr)

def exit_game(stdscr):
    global running
    running = False
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    print("\nGame exited.")

if __name__ == "__main__":
    curses.wrapper(main)
