import guesser
import random

f = open('valid-wordle-words.txt', 'r')
words = []

for line in f:
    words.append(line[0:5])

# wordle
class Wordle:
    def __init__(self):
        self.answer = random.choice(words)
        self.attempts = []

    def processGuess(self, guess):
        self.attempts.append(guess)
        if guess == self.answer:
            # self.congratulate()
            return 'Victory'
        
        currWord = ''
        knownLetters = ''
        badLetters = []

        for i in range(0, 5):
            if guess[i] == self.answer[i]:
                currWord += guess[i]
            else:
                currWord += '_'

            letters = {letter for letter in self.answer} 
            if guess[i] in letters and guess[i] != self.answer[i]:
                letters.remove(guess[i])
                knownLetters += guess[i]
            else:
                knownLetters += '_'
            
            if guess[i] not in self.answer:
                badLetters.append(guess[i])

        return [currWord, knownLetters, badLetters]
    
    def congratulate(self):
        print(f'Congrats! You got the word {self.answer}!')

    def reveal(self):
        print(self.answer)

# wordle bot
class Player:
    def __init__(self, guesses, frequency):
        self.guesses = words.copy()
        self.currWord = '_____'
        self.knownLetters = '_____'
        self.badLetters = []
        self.frequency = frequency
    
    def update(self, currWord, knownLetters, badLetters):
        self.currWord = currWord
        self.knownLetters = knownLetters
        self.badLetters = badLetters

    def guess(self):
        self.guesses = guesser.scanGuesses(self.guesses, self.currWord, self.knownLetters, self.badLetters) # narrow down the guess list
        self.guesses = guesser.scoreGuesses(self.guesses, self.frequency) # sort guess list
        return self.guesses[0]


def play(player, wordle):
    while len(wordle.attempts) < 7:
        guess = player.guess()
        feedback = wordle.processGuess(guess)
        if feedback == 'Victory':
            break
        player.currWord = feedback[0]
        player.knownLetters = feedback[1]
        player.badLetters = feedback[2]
    
    attempts = len(wordle.attempts)
    return attempts

def average(numbers):
    total = sum(numbers)
    return total / len(numbers)

def testAccuracy(reps, *freqs):
    attempts = []
    for i in range(len(freqs)):
        attempts.append([])

    for i in range(reps):
        wordle = Wordle()
        count = 0
        for frequency in freqs:
            bot = Player(words, frequency)
            wordle.attempts = []
            attempts[count].append(play(bot, wordle))
            count += 1
    
    avgAttempts = []
    for group in attempts:
        avgAttempts.append(average(group))
    
    for avg in avgAttempts:
        iteration = avgAttempts.index(avg) + 1
        print('Test ' + str(iteration))
        print(avg)
        

# program starts here

freq1 = 'etaoinshrdlcumwfgypbvkjxqz'
freq2 = 'esaoriltnudpmychgbkfwvzjxq'
freq3 = 'etaoinsrhdlucmfywgpbvkxqjz'

testAccuracy(10, freq1, freq2, freq3)