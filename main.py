f = open('valid-wordle-words.txt', 'r')
# frequency = 'etaoinshrdlcumwfgypbvkjxqz' # based on morse code
frequency = 'esaoriltnudpmychgbkfwvzjxq'

current_word = '_____'
known_letters = '_____'
bad_letters = []
guesses = []
recommended = []

# todo
# add idiot proofing to inputs (ex: repeat letters, non-letters)
# make scanGuesses more efficient
# score guesses

for line in f:
    guesses.append(line[0:5])

def scanGuesses():
    global guesses
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

# def removeDuplicateLetters(list):
#     newList = []
#     for word in list:
#         wordSet = {letter for letter in word}
#         if len(wordSet) > 4:
#             newList.append(word)
    
#     return newList

def hasDuplicateLetters(word):
    wordSet = {letter for letter in word}
    if len(wordSet) < 5:
        return True    
    return False

def scoreGuesses(list):
    global frequency
    scoreKeeper = {}
    for word in list:
        score = 0
        for letter in word:
            score += (26 - frequency.index(letter))
        if hasDuplicateLetters(word):
            score /= 2
        scoreKeeper[word] = score

    sortedScores = dict(sorted(scoreKeeper.items(), key=lambda item: item[1], reverse=True))
    sortedWords = sortedScores.keys()
    return sortedWords

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
    # if len(guesses) > 10:
    #     recommended = (removeDuplicateLetters(guesses))
    #     print(recommended)
    print(scoreGuesses(guesses))