from pickle import TRUE
import string
import random

### Defining the Class of Learning Words

class Word:
    def __init__(self,English,Faroese):
        #attributes
        self.Faroese = Faroese
        self.English = English

def wordIter(words):
    words = words.split('\n')
    possibleWords = []
    for line in words:
        word = line.split(',')
        possibleWords.append(Word(word[0],word[1]))
    return possibleWords

words = """Car,Bilur
Lion,Leyva
Frog,Froskur"""

allWords = wordIter(words)


def gameplay():
    playToggle = TRUE
    print("Welcome to Bran's language learning game.")
    while playToggle == TRUE:
        round()


        # chosenWord = random.choice(allWords)
        # desiredWord = chosenWord.Faroese
        # translation = chosenWord.English
        # wordLength = []
        # wordLetters = []
        # guesses = []
        # updateOutput = []
        # for letter in desiredWord:
        #     wordLength.append('-')
        #     wordLetters.append(letter.lower())
        # output = ''.join(wordLength)
        # # print(desiredWord,":",output,'\n',wordLetters)
        # print(wordLength)
        # playerGuess = input()
        # if playerGuess.lower() in wordLetters:
        #     print('Good Guess!')
        #     guesses.append(playerGuess.lower())    
        # else:
        #     print('Try Again')
        #     guesses.append(playerGuess.lower())
        # for letter in desiredWord:
        #     if letter in guesses:
        #         updateOutput.append(letter)
        #     else:
        #         updateOutput.append('-')
        # print(updateOutput)

def round():
    round = TRUE
    roundWord = random.choice(allWords)
    targetWord = roundWord.Faroese
    translation = roundWord.English
    roundGuesses = []
    wordLetters = []
    display = []
    for letter in targetWord:
        wordLetters.append(letter.lower())
    for letter in wordLetters: 
        display.append('-')
    print('Your word is:',display)
    while round == TRUE:
        display = []
        playerGuess = input()
        if playerGuess.lower() in wordLetters:
            print('Good guess!')
            roundGuesses.append(playerGuess)
        else:
            print('Try again!')
            roundGuesses.append(playerGuess)
        for letter in wordLetters:
            if letter in roundGuesses:
                display.append(letter.lower())
            else:
                display.append('-')
        print(display)
    

gameplay()
