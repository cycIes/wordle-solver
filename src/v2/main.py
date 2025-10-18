import word_tree as tree
from text import Color, modifyText

# start of program

print('\033c', end='', flush=True) # to clear the terminal with ANSI code

EMPTY = '_____'
EXAMPLE = modifyText(Color.GREEN,'w') + modifyText(Color.YELLOW,'o') + modifyText(Color.YELLOW,'r') + 'ds'

current_word = EMPTY
close_letters = EMPTY
bad_letters = []

def printWarning(text):
    print(modifyText(Color.RED, text))

def includesNonalphabetic(letters):
    for letter in letters:
        if not letter.isalpha() and letter.lower() != '_':
            return True
    
    return False

def invalidInput(word):
    if len(word) != 5:
        printWarning('Please provide a 5 length combination of letters or underscores.')
        return True
    
    if includesNonalphabetic(word):
        printWarning('Please only include alphabetical characters or underscores.')
        return True
    
    return False

def closeLetterConflict(close_letters, correct_letters):
    for i in range(len(close_letters)):
        if close_letters[i] != '_' and correct_letters[i] != '_':
            printWarning('Letters conflict with already known letters in the correct spot.')
            return True
        if close_letters[i] in bad_letters:
            printWarning('Cannot provide letters that are known to be not in the word.')
            return True
    
    return False

def badLetterConflict(bad_letters, correct_letters, close_letters):
    for letter in bad_letters:
        if letter in correct_letters or letter in close_letters:
            printWarning('Letters conflict with already known letters.')
            return True
        
    return False

# program starts here

while '_' in current_word:
    print(f'\nCurrent word: {current_word}')
    print(f'Letters not in word: {",".join(bad_letters)}')

    print(f'\nWhat are the current known letters in the correct spot (in {modifyText(Color.GREEN, "green")})?')
    print('Use underscore for unknown letters. Type q to quit.')
    print(f'Example: for a feedback of {EXAMPLE} type w____.')
    correct_letters = input().lower()
    if correct_letters == '':
        correct_letters = '_____'
    elif correct_letters == 'q':
        break
        
    if invalidInput(correct_letters):
        continue

    print(f'\nWhat are the known letters not in the correct spot (in {modifyText(Color.YELLOW, "yellow")})?')
    print('Use their exact positions with underscores in non-yellow spaces.')
    print(f'Example: for a feedback of {EXAMPLE} type _or__.')
    close_letters = input().lower()
    
    if invalidInput(close_letters) or closeLetterConflict(close_letters, correct_letters):
        continue

    print('\nWhat are letters not in the word (in gray)?')
    print('Do not leave a space between multiple letters.')
    print(f'Example: for a feedback of {EXAMPLE} type ds')
    letters = input()
    
    if includesNonalphabetic(letters) or badLetterConflict(letters, correct_letters, close_letters):
        continue

    for letter in letters:
        if letter not in bad_letters and not includesNonalphabetic(letter):
            bad_letters.append(letter.lower())

    current_word = correct_letters

    possible_words = []
    tree.updatePossibleWords(tree.letter_tree, possible_words, current_word, close_letters, bad_letters)
    possible_words = tree.sortPossibleWords(possible_words)
    no_duplicates = tree.filterOutRepeatingLetters(possible_words)
    # print(possible_words)
    print(f'\nThere are {len(possible_words)} possible words')
    print(f'Top five words: {", ".join([word["word"] for word in possible_words[0:5]])}')
    print(f'Top five words without duplicates: {", ".join([word["word"] for word in no_duplicates[0:5]])}')