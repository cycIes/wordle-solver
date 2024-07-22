f = open('valid-wordle-words.txt', 'r')
frequency = 'etaoinshrdlcumwfgypbvkjxqz' # based on morse code
# frequency = 'esaoriltnudpmychgbkfwvzjxq' # based on the text file

current_word = '_____'
known_letters = '_____'
bad_letters = []
guesses = []

# TODO
# add idiot proofing to inputs (ex: repeat letters, non-letters)
# make scanGuesses more efficient
# tune guess scoring

for line in f:
    guesses.append(line[0:5]) # to remove the \n after each word

def scanGuesses(guesses):
    global known_letters
    good_guesses = guesses.copy()

    for word in guesses:
        removed = False

        for letter in current_word:
            if letter == '_':
                continue
            if letter not in word:
                good_guesses.remove(word)
                removed = True
                break
            elif letter != word[(current_word.index(letter))]:
                good_guesses.remove(word)
                removed = True
                break

        if removed == True:
            continue
        
        for letter in known_letters:
            if letter == '_':
                continue
            if letter not in word:
                good_guesses.remove(word)
                removed = True
                break
            elif letter == word[(known_letters.index(letter))]:
                good_guesses.remove(word)
                removed = True
                break
        
        if removed == True:
            continue

        for letter in bad_letters:
            if letter in word:
                good_guesses.remove(word)
                break

    guesses = good_guesses.copy()
    return guesses

def hasDuplicateLetters(word):
    wordSet = {letter for letter in word}
    if len(wordSet) < 5:
        return True    
    return False

def vowelCount(word):
    count = 0
    vowels = 'aeiou' # not counting y because it is special
    for letter in word:
        if letter in vowels:
            count += 1
    
    return count

def scoreGuesses(guesses):
    global frequency
    scoreKeeper = {}
    for word in guesses:
        score = 0
        for letter in word:
            score += (26 - frequency.index(letter))
        if vowelCount(word) > 2:
            score *= .9
        if hasDuplicateLetters(word):
            score /= 2
        scoreKeeper[word] = score

    sortedScores = dict(sorted(scoreKeeper.items(), key=lambda item: item[1], reverse=True))
    sortedWords = list(sortedScores.keys())
    return sortedWords

# start of program

print('\033c', end='', flush=True) # to clear the terminal with ANSI code

while '_' in current_word:
    current_word = input('What are the current known letters in the correct spot (in green)? Use underscore for unknown letters. Type q to quit.\n')
    if current_word == '':
        current_word = '_____'
    elif current_word == 'q':
        break
    known_letters = input('What are the known letters not in the correct spot (in yellow)? Use their exact positions with underscores in non-yellow spaces.\n')
    letters = input('What are letters not in the word (in gray)? Do not leave a space between multiple letters.\n')
    for letter in letters:
        bad_letters.append(letter)

    guesses = scanGuesses(guesses)
    sortedGuesses = scoreGuesses(guesses)
    print(sortedGuesses)
    print(f'There are {len(sortedGuesses)} possible words')
    print('Top three: ' + str(sortedGuesses[0:3]))