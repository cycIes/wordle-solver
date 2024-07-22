# frequency finder experiment for wordle solver
f = open('valid-wordle-words.txt', 'r')
frequency = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# make file readable to code
words = ''
for line in f:
    words += line[0:5]

for letter in alphabet:
    score = words.count(letter)
    frequency[letter] = score

sorted_frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
print(sorted_frequency)

ordered_letters = ''.join(list(sorted_frequency.keys()))
print(ordered_letters)