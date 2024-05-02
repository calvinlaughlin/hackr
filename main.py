import curses

class Puzzle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def display(self, stdscr):
        stdscr.addstr(self.question)

    def solve(self, input):
        return input.strip() == self.answer

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Set up curses options
    curses.curs_set(1)  # Show the cursor
    stdscr.nodelay(0)   # Wait for user input
    stdscr.keypad(True) # Enable keypad mode

    # Setup the initial game state
    puzzles = [
        Puzzle("Question 1: What is 2+2? ", "4"),
        Puzzle("Question 2: What is the capital of France? ", "Paris"),
        Puzzle("Question 3: What color is the sky on a clear day? ", "Blue"),
        Puzzle("Question 4: What is the opposite of up? ", "Down"),
        Puzzle("Question 5: What device are you using? ", "Computer")
    ]
    current_puzzle = 0
    max_puzzles = len(puzzles)

    while current_puzzle < max_puzzles:
        stdscr.clear()
        # Display the current puzzle
        puzzle = puzzles[current_puzzle]
        puzzle.display(stdscr)

        # Refresh to show output
        stdscr.refresh()

        # Initialize an empty answer string
        answer = ""
        while True:
            # Wait for user input (character by character)
            ch = stdscr.getch()
            if ch == 10:  # Enter key is pressed
                break
            elif ch == 127 or ch == 8:  # Handle backspace for deletion
                answer = answer[:-1]
                stdscr.delch()  # Delete the last character on the screen
            else:
                # Append the character to the answer string and display it
                answer += chr(ch)
                stdscr.addch(ch)

        # Process input
        if puzzle.solve(answer):
            stdscr.addstr("\nCorrect! Press any key to continue.")
            stdscr.refresh()
            stdscr.getch()
            current_puzzle += 1
        else:
            stdscr.addstr("\nIncorrect! Try again.")
            stdscr.refresh()
            stdscr.getch()

    stdscr.addstr("\nGame Over! Press any key to exit.")
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)
