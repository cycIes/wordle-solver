f = open('valid-wordle-words.txt', 'r')

#possible_letters = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
current_word = '_____'
known_letters = '_____'
bad_letters = []
guesses = []
recommended = []

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
    global known_letters
    good_guesses = guesses.copy()

    for word in guesses:
        for letter in current_word:
            if letter == '_':
                continue
            if letter not in word:
                good_guesses.remove(word)
                break
            elif letter != word[(current_word.index(letter))]:
                good_guesses.remove(word)
                break
    guesses = good_guesses.copy()
    
    for word in guesses:
        for letter in known_letters:
            if letter == '_':
                continue
            if letter not in word:
                good_guesses.remove(word)
                break
            elif letter == word[(known_letters.index(letter))]:
                good_guesses.remove(word)
                break
    guesses = good_guesses.copy()

    for word in guesses:
        for letter in bad_letters:
            if letter in word:
                good_guesses.remove(word)
                break

    guesses = good_guesses.copy()

def removeDuplicateLetterWords(list):
    newList = []
    for word in list:
        wordSet = {letter for letter in word}
        if len(wordSet) > 4:
            newList.append(word)
    
    return newList

while '_' in current_word:
    current_word = input('What are the current known letters in the correct spot (in green)? Use underscore for unknown letters. Enter to quit.\n')
    if current_word == '':
        break
    known_letters = input('What are the known letters not in the correct spot (in yellow)? Use their exact positions with underscores in non-yellow spaces.\n')
    # for letter in letters:
    #     known_letters.append(letter)
    letters = input('What are letters not in the word (in gray)? Do not leave a space between multiple letters.\n')
    for letter in letters:
        #possible_letters.remove(letter)
        bad_letters.append(letter)
    
    # remove later
    print(current_word)
    print(known_letters)
    print(bad_letters)

    scanGuesses()
    if len(guesses) > 10:
        recommended = (removeDuplicateLetterWords(guesses))
        print(recommended)
    else:
        print(guesses)
    
    # print('Top 3 recommended guesses: ')