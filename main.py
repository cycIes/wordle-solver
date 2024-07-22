f = open('valid-wordle-words.txt', 'r')
print(len(f.readlines()))

possible_letters = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
word = '_____'
known_letters = []

# todo
# add idiot proofing to inputs (ex: repeat letters, non-letters)

while '_' in word:
    word = input('What are the current known letters in the correct spot (in green)? Use underscore for unknown letters.\n')
    letters = input('What are the known letters not in the correct spot (in yellow)? Do not leave a space between multiple letters.\n')
    for letter in letters:
        known_letters.append(letter)
    letters = input('What are letters not in the word (in gray)? Do not leave a space between multiple letters.\n')
    for letter in letters:
        possible_letters.remove(letter)
    
    # remove later
    print(word)
    print(known_letters)
    print(possible_letters)

    print('Top 3 recommended guesses: ')