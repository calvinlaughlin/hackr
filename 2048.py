import curses
from random import randrange, choice

def main(stdscr):
    # Initialize the game
    def init():
        return 'Game', [[0] * 4 for _ in range(4)], 0

    def new_game():
        return 'Game', [[0] * 4 for _ in range(4)], 0

    def add_new_tile(mat):
        new_element = 4 if randrange(100) > 89 else 2
        (i, j) = choice([(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0])
        mat[i][j] = new_element
        return mat

    def transpose(mat):
        return [list(row) for row in zip(*mat)]

    def invert(mat):
        return [row[::-1] for row in mat]

    def flatten(mat):
        return [cell for row in mat for cell in row]

    def game_state(mat):
        if any(2048 in row for row in mat):
            return 'Win'
        if not any(0 in row for row in mat):
            for i in range(4):
                for j in range(4):
                    if i + 1 < 4 and mat[i][j] == mat[i + 1][j]:
                        return 'Game'
                    if j + 1 < 4 and mat[i][j] == mat[i][j + 1]:
                        return 'Game'
            return 'Lose'
        return 'Game'

    def move(mat):
        def tighten(mat):
            new_mat = [[0] * 4 for _ in range(4)]
            for i in range(4):
                pos = 0
                for j in range(4):
                    if mat[i][j] != 0:
                        new_mat[i][pos] = mat[i][j]
                        pos += 1
            return new_mat

        def merge(mat):
            new_score = 0
            for i in range(4):
                for j in range(3):
                    if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                        mat[i][j] *= 2
                        mat[i][j + 1] = 0
                        new_score += mat[i][j]
            return mat, new_score

        mat = tighten(mat)
        mat, new_score = merge(mat)
        mat = tighten(mat)
        return mat, new_score

    def move_left(mat):
        return move(mat)

    def move_right(mat):
        mat = invert(mat)
        mat, score = move(mat)
        mat = invert(mat)
        return mat, score

    def move_up(mat):
        mat = transpose(mat)
        mat, score = move(mat)
        mat = transpose(mat)
        return mat, score

    def move_down(mat):
        mat = transpose(mat)
        mat, score = move_right(mat)
        mat = transpose(mat)
        return mat, score

    def draw_banner(stdscr):
        banner = [
            " .-----.   .----.      .---.    .-----.   ",
            "/ ,-.   \ /  ..  \    / .  |   /  .-.  \  ",
            "'-'  |  |.  /  \  .  / /|  |   \  \_.' /  ",
            "   .'  / |  |  '  | / / |  |_  /  .-. '.  ",
            " .'  /__ '  \  /  '/  '-'    ||  |   |  | ",
            "|       | \  `'  / `----|  |-' \  '-'  /  ",
            "`-------'  `---''       `--'    `----''   "
        ]
        for i, line in enumerate(banner):
            stdscr.addstr(i, 0, line, curses.color_pair(1))

    def draw(stdscr, state, mat, score):
        stdscr.clear()
        draw_banner(stdscr)
        if state == 'Game':
            for i in range(4):
                for j in range(4):
                    num = mat[i][j]
                    if num == 0:
                        stdscr.addstr(i * 2 + 10, j * 5, '0'.center(5), curses.color_pair(1))
                    else:
                        color_pair = number_colors.get(num, 1)
                        stdscr.addstr(i * 2 + 10, j * 5, str(num).center(5), curses.color_pair(color_pair))
            stdscr.addstr(23, 0, f'Score: {score}')
        elif state == 'Win':
            stdscr.addstr(5, 5, 'You Win!')
        elif state == 'Lose':
            stdscr.addstr(5, 5, 'Game Over!')
        stdscr.refresh()

    # Initialize color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLACK)

    number_colors = {
        2: 2,
        4: 3,
        8: 4,
        16: 5,
        32: 6,
        64: 7,
        128: 8,
        256: 2,
        512: 3,
        1024: 4,
        2048: 5
    }

    state, mat, score = init()
    mat = add_new_tile(mat)
    mat = add_new_tile(mat)
    draw(stdscr, state, mat, score)

    key_actions = {
        curses.KEY_UP: move_up,
        curses.KEY_DOWN: move_down,
        curses.KEY_LEFT: move_left,
        curses.KEY_RIGHT: move_right,
        ord('r'): new_game,
        ord('R'): new_game
    }

    while True:
        key = stdscr.getch()
        if key in (ord('q'), ord('Q')):
            break

        if key in key_actions:
            action = key_actions[key]
            if action == new_game:
                state, mat, score = new_game()
                mat = add_new_tile(mat)
                mat = add_new_tile(mat)
            else:
                if state == 'Game':
                    new_mat, new_score = action(mat)
                    if new_mat != mat:
                        mat = add_new_tile(new_mat)
                        score += new_score
                    state = game_state(mat)
            draw(stdscr, state, mat, score)

curses.wrapper(main)
