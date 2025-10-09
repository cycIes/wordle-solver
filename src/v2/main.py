import word-tree as tree

# start of program

print('\033c', end='', flush=True) # to clear the terminal with ANSI code

current_word = '_____'

while '_' in current_word:
    current_word = input('What are the current known letters in the correct spot (in green)? Use underscore for unknown letters. Type q to quit.\n')
    if current_word == '':
        current_word = '_____'
    elif current_word == 'q':
        break
    known_letters = input('What are the known letters not in the correct spot (in yellow)? Use their exact positions with underscores in non-yellow spaces.\n')
    letters = input('What are letters not in the word (in gray)? Do not leave a space between multiple letters.\n')
    for letter in letters:
        guesser.bad_letters.append(letter)

    guesser.guesses = guesser.scanGuesses(guesser.guesses, current_word, known_letters, guesser.bad_letters)
    sorted_guesses = guesser.scoreGuesses(guesser.guesses, guesser.frequency)
    print(sorted_guesses)
    print(f'There are {len(sorted_guesses)} possible words')
    print('Top three: ' + str(sorted_guesses[0:3]))