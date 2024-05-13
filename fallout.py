import curses
import random
import string

def pick_words(all_words, length=4, num_words=10):
    words = [word.upper() for word in all_words if len(word) == length]
    return random.sample(words, num_words)

def add_gibberish(words, total_gibberish_length=40):
    gibberish_words = []
    for word in words:
        prefix_length = random.randint(0, total_gibberish_length)
        suffix_length = total_gibberish_length - prefix_length
        prefix = ''.join(random.choice(string.punctuation + string.digits) for _ in range(prefix_length))
        suffix = ''.join(random.choice(string.punctuation + string.digits) for _ in range(suffix_length))
        gibberish_words.append(prefix + word + suffix)
    return gibberish_words

def display_words(stdscr, words, lives):
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    
    instruction_text = "Guess the correct word (navigate with arrows, select with Enter):"
    lives_text = "Lives: " + '$' * lives
    lives_text_padded = lives_text + (' ' * (11 - len(lives_text)))
    stdscr.addstr(0, (max_x - len(instruction_text)) // 2, instruction_text)
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(1, (max_x - len(lives_text_padded)) // 2, lives_text_padded)
    stdscr.attroff(curses.color_pair(1))
    for idx, word in enumerate(words):
        stdscr.addstr(idx + 3, (max_x - len(word)) // 2, word)
    stdscr.refresh()

def get_matching_letters(guess, correct_word):
    return sum([1 for g, c in zip(guess, correct_word) if g == c])

def game_loop(stdscr, gibberish_words, clean_words, correct_word):
    position = 0
    max_y, max_x = stdscr.getmaxyx()
    history = []
    lives = 4  # Set the number of lives

    

    display_words(stdscr, gibberish_words, lives)
    while True:
        for idx, word in enumerate(gibberish_words):
            if idx == position:
                start = word.index(clean_words[idx])
                end = start + len(clean_words[idx])
                word_start = (max_x - len(word)) // 2
                stdscr.addstr(idx + 3, word_start, word[:start])
                stdscr.addstr(idx + 3, word_start + start, clean_words[idx], curses.A_REVERSE)
                stdscr.addstr(idx + 3, word_start + end, word[end:])
            else:
                stdscr.addstr(idx + 3, (max_x - len(word)) // 2, word)

        key = stdscr.getch()
        if key == curses.KEY_UP and position > 0:
            position -= 1
        elif key == curses.KEY_DOWN and position < len(clean_words) - 1:
            position += 1
        elif key == 10:  # Enter key
            clean_word = clean_words[position]
            if clean_word != correct_word:
                lives -= 1
                display_words(stdscr, gibberish_words, lives)  # Update display with new lives count
            matches = get_matching_letters(clean_word, correct_word)
            feedback_msg = f"> Chosen: {clean_word} - Matches: {matches} correct positions. Lives remaining: {lives}"
            history.append(feedback_msg)
            for idx, msg in enumerate(history):
                stdscr.addstr(idx + len(clean_words) + 5, (max_x - len(msg)) // 2, msg)
            stdscr.refresh()
            if clean_word == correct_word:
                stdscr.addstr(max_y - 2, (max_x - len("Correct! Press any key to exit.")) // 2, "Correct! Press any key to exit.", curses.A_BOLD)
                stdscr.refresh()
                stdscr.getch()
                break
            if lives <= 0:
                stdscr.addstr(max_y - 2, (max_x - len("Out of lives! Game over. Press any key to exit.")) // 2, "Out of lives! Game over. Press any key to exit.", curses.A_BOLD)
                stdscr.refresh()
                stdscr.getch()
                break

def main(stdscr):
    curses.curs_set(0)
    all_words = ["shot", "hurt", "sell", "give", "sure", "gear", "fire", "sent", "glow", "week", "ones", "sick"]
    clean_words = pick_words(all_words, num_words=len(all_words))
    gibberish_words = add_gibberish(clean_words)
    correct_word = random.choice(clean_words)
    game_loop(stdscr, gibberish_words, clean_words, correct_word)

curses.wrapper(main)
