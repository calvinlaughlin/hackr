import curses
import time

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(0)  # Make getch() blocking
    curses.start_color()  # Initialize colors

    # Define color pair for blue text
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

    # Define levels
    levels = [
        {
            "paragraph1": "DuriNg the other parade, a drummer showcased remarkable skill, captivating the audience with rhythmic beats.", 
            "blue_letters": ['r', 'o', 'a', 'd', 'm', 'a', 'n'],
            "password": "roAdMan"
        },
        {
            "paragraph1": "wiLLow trees swaYed gEntLy in the cooL breeze by The Lakeside.",
            "blue_letters": ['w', 'i', 'l', 'l'],
            "password": "wiL"
        },
        {
            "paragraph1": "shE wATched as the mischievous cat Tried to steaL a piece of fish from the tabLe.",
            "blue_letters": ['s', 't', 'e', 'a', 'l'],
            "password": "sTeaL"
        }
    ]

    lives = 3
    for level in range(3):
        if lives <= 0:
            break
        while not play_level(stdscr, levels[level], level + 1, lives):
            lives -= 1
            if lives <= 0:
                break

    stdscr.clear()
    if lives > 0:
        stdscr.addstr(0, 0, "Congratulations! You've beaten the puzzle!", curses.A_BOLD)
    else:
        stdscr.addstr(0, 0, "Game Over! Better luck next time.", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getch()

def display_paragraph(stdscr, paragraph, blue_letters, y):
    for i, char in enumerate(paragraph):
        if char in blue_letters:
            stdscr.addstr(y, i, char, curses.color_pair(1))
        else:
            stdscr.addstr(y, i, char)

def play_level(stdscr, level, level_number, lives):
    stdscr.clear()
    curses.echo()
    stdscr.nodelay(1)  # Make getstr() non-blocking

    # Display level info
    stdscr.addstr(0, 0, f"Level {level_number}", curses.A_BOLD)
    stdscr.addstr(1, 0, f"Lives: {lives}", curses.A_BOLD)
    stdscr.addstr(2, 0, f"You have 1 minute to find the password. Good luck!")
    stdscr.addstr(3, 0, f"Hint: Enter letters as they first appear.")
    stdscr.addstr(4, 0, f"{'-' * 80}")

    # Display paragraphs with blue letters
    display_paragraph(stdscr, level["paragraph1"], level["blue_letters"], 7)

    # Prompt for password
    stdscr.addstr(10, 0, "Enter the password: ")
    stdscr.refresh()

    start_time = time.time()
    entered_password = ""
    input_buffer = []

    while time.time() - start_time < 60:
        remaining_time = 60 - (time.time() - start_time)
        stdscr.addstr(1, 20, f"Time left: {int(remaining_time)} seconds ")
        stdscr.refresh()

        try:
            char = stdscr.getch()
            if char != -1:
                if char == ord('\n'):
                    entered_password = "".join(input_buffer)
                    break
                elif char == 127:  # Backspace
                    if input_buffer:
                        input_buffer.pop()
                        stdscr.addstr(10, 20 + len(input_buffer), ' ')
                else:
                    input_buffer.append(chr(char))
                    stdscr.addstr(10, 20 + len(input_buffer) - 1, chr(char))
                stdscr.refresh()
        except curses.error:
            pass

    if entered_password == level["password"]:
        stdscr.addstr(11, 0, "Correct! Moving to the next level...", curses.A_BOLD)
        stdscr.refresh()
        time.sleep(2)
        return True
    else:
        stdscr.addstr(11, 0, "Incorrect password or time's up. You lost a life.", curses.A_BOLD)
        stdscr.refresh()
        time.sleep(2)
        return False

curses.wrapper(main)
