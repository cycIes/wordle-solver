f = open('valid-wordle-words.txt', 'r')

#possible_letters = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
word = '_____'
known_letters = []
bad_letters = []
guesses = []

# todo
# add idiot proofing to inputs (ex: repeat letters, non-letters)
# cannot tell when a possible letter is not supposed to be in a position
# maybe make a list for each position?
# code is not efficient enough, combine searches in scanGuesses

#len(f.readlines())

# for line in f:
#     print(line)
# took 2.61 seconds

for line in f:
    guesses.append(line[0:5])

def scanGuesses():
    global guesses
    good_guesses = guesses.copy()
    for word in guesses:
        for letter in known_letters:
            if letter not in word:
                good_guesses.remove(word)
                break
    guesses = good_guesses.copy()

    for word in guesses:
        for letter in bad_letters:
            if letter in word:
                good_guesses.remove(word)
                break

    guesses = good_guesses.copy()

while '_' in word:
    word = input('What are the current known letters in the correct spot (in green)? Use underscore for unknown letters.\n')
    letters = input('What are the known letters not in the correct spot (in yellow)? Use their exact positions with underscores in non-yellow spaces.\n')
    for letter in letters:
        known_letters.append(letter)
    letters = input('What are letters not in the word (in gray)? Do not leave a space between multiple letters.\n')
    for letter in letters:
        #possible_letters.remove(letter)
        bad_letters.append(letter)
    
    # remove later
    print(word)
    print(known_letters)
    print(bad_letters)

    scanGuesses()
    print(guesses)
    # print('Top 3 recommended guesses: ')