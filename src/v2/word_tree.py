import random

word_list = open('src/lists/valid-wordle-words.txt', 'r')

class Node:
    def __init__(self, letter, level):
        self.letter = letter
        self.level = level
        self.strength = 1
        self.nodes = []

def editTree(word, level, tree):
    if word == '':
        return
    
    letter = word[0]
    for node in tree:
        if (node.letter == letter):
            node.strength += 1
            editTree(word[1:len(word)], level + 1, node.nodes)
            break
    else:
        new_node = Node(letter, level)
        tree.append(new_node)
        editTree(word[1:len(word)], level + 1, new_node.nodes)

def getRandomWord(tree):
    if len(tree) == 0:
        return ''
    randNode = random.choice(tree)
    return randNode.letter + getRandomWord(randNode.nodes)

def findPossibleWords(tree, possible_words, current_word, freq, locked, unlocked, bad_letters):
    letter_pos = len(current_word)

    if len(tree) == 0:
        for letter in unlocked:
            if letter not in current_word and letter != '_':
                return
        possible_words.append({'word': current_word, 'freq': freq})
    for node in tree:
        if node.letter in bad_letters:
            continue
        if node.letter == unlocked[letter_pos]:
            continue
        if locked[letter_pos] != '_' and node.letter != locked[letter_pos]:
            continue
        findPossibleWords(node.nodes, possible_words, current_word + node.letter, freq + node.strength, locked, unlocked, bad_letters)

def updatePossibleWords(tree, possible_words, locked, unlocked, bad_letters):
    findPossibleWords(tree, possible_words, '', 0, locked, unlocked, bad_letters)

def sortPossibleWords(possible_words):
    return sorted(possible_words, key = lambda d: d['freq'], reverse = True)

def wordHasDuplicates(word):
    for letter in word:
        if word.count(letter) > 1:
            return True
    
    return False

def filterOutRepeatingLetters(word_list):
    filtered = []
    for word in word_list:
        if not wordHasDuplicates(word['word']):
            filtered.append(word)
    
    return filtered


letter_tree = []

for line in word_list:
    word = line[0:len(line)-1]
    editTree(word, 0, letter_tree)

# possible_words = []
# updatePossibleWords(letter_tree, possible_words, '_____', '_____', [])
# possible_words = sorted(possible_words, key = lambda d: d['freq'], reverse = True)
# print(possible_words)