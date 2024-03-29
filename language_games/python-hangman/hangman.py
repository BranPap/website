from pickle import FALSE, TRUE
import string
import random

### Defining the Class of Learning Words

class Word:
    def __init__(self,English,Faroese):
        #attributes
        self.Faroese = Faroese
        self.English = English

### Defining the iterate function that will take a list of input strings and return them as objects to be used in gameplay

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
    print("Welcome to Bran's language learning game. You will get a random word in Faroese, and have to guess the word by providing the program with 1-letter guesses. Once you guess the word, you'll be asked to translate it into English! Easy enough? Let's get started!")
    print('\n')
    while playToggle == TRUE:
        round()

def translate(roundWord):
    translationPlay = TRUE
    print('Now it\'s time to translate this word into English!')
    print('What does',roundWord.Faroese,'mean in English?')
    translationAnswer = roundWord.English.lower()
    while translationPlay == TRUE:
        translationGuess = input()
        if translationGuess.lower() == translationAnswer:
            print('Yes, you got it!')
            print('Would you like to try another word?')
            playAgainAnswer = input()
            if playAgainAnswer.lower() == "yes":
                return TRUE
            else:
                print('Okay, goodbye!')
                quit()
        else: 
            print('Hmm, I don\'n think that\'s quite right. Try again!')

def check(wordLetters, roundGuesses, roundWord):
    errors = 0
    translationComplete = FALSE
    for letter in wordLetters:
        if letter not in roundGuesses:
            errors += 1
    if errors == 0:
        print('You guessed the word!')
        # translate(roundWord)
        translationComplete = translate(roundWord)
    if translationComplete == TRUE:
        return TRUE

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
        if len(playerGuess) != 1:
            print('Your guess must be exactly one character long!')
        else: 
            if playerGuess.lower() in wordLetters:
                print('Good guess!')
                roundGuesses.append(playerGuess.lower())
            else:
                print('Try again!')
                roundGuesses.append(playerGuess.lower())
        for letter in wordLetters:
            if letter in roundGuesses:
                display.append(letter.lower())
            else:
                display.append('-')
        print(display)
        roundEnd = check(wordLetters, roundGuesses, roundWord)
        if roundEnd == TRUE:
            round = FALSE
            allWords.remove(roundWord)
    if len(allWords) == 0:
        print('You\'ve completed all the words in the game!')
    
gameplay()