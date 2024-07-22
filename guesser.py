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

def scanGuesses(guesses, green, yellow, gray):
    good_guesses = guesses.copy()

    for word in guesses:
        removed = False

        for letter in green:
            if letter == '_':
                continue
            if letter not in word:
                good_guesses.remove(word)
                removed = True
                break
            elif letter != word[(green.index(letter))]:
                good_guesses.remove(word)
                removed = True
                break

        if removed == True:
            continue
        
        for letter in yellow:
            if letter == '_':
                continue
            if letter not in word:
                good_guesses.remove(word)
                removed = True
                break
            elif letter == word[(yellow.index(letter))]:
                good_guesses.remove(word)
                removed = True
                break
        
        if removed == True:
            continue

        for letter in gray:
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