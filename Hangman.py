# Hangman.py
# The game of Hangman. You only get 6 guesses. Have fun!
# Andrew Alonso
# 3/12/2021

import re
import random

def getWord():
    ''' Finds a random word from given textfile.'''

    word = (random.choice(open("wordsForHangman.txt","r").read().split()))
    word = word.lower()
    
    pregame(word)
    
def pregame(word):
    ''' Gets variables needed for when the game has started. '''
    
    chances = 6        # Number of incorrect choices allowed
    
    # How much char's are left to fill, & underscores of len(word) is result
    leftToFill = len(word)
    result = ['_'] * len(word)
    
    print(f'''
      ______
     |     |
           |
           |
           |
       ____|____ ''')
    
    # Removes commas brackets and quotes for printing
    res = str(result).replace(","," ").replace("["," ").replace("]","").replace("'","")
    print(f'{res}\n')
    
    # List of total letters used & list of incorrect letters used
    lettersUsed = []
    incorrect = []
    
    # Start game of Hangman
    start(result, word, leftToFill, lettersUsed, incorrect, chances)

def start(res, word, leftToFill, charUsed, incorrect, c):
    ''' Starts the game of hangman. '''

    userLetter = str(input(f'Enter a letter: '))
    userLetter = userLetter.lower()
    
    # If incorrect input is entered. Ex: not a character, <1 input, >1 input
    pattern = re.compile("[a-z]+")
    if pattern.fullmatch(userLetter) is None:
        print('Type a letter that is a-z only.\n')
        start(res, word, leftToFill, charUsed, incorrect, c)
        
    elif len(userLetter) < 1:
        print('Type a letter a-z.\n')
        start(res, word, leftToFill, charUsed, incorrect, c)
        
    elif len(userLetter) > 1:
        print('Type only 1 letter at a time.\n')
        start(res, word, leftToFill, charUsed, incorrect, c)
    
    # Checks if character has already been used before
    for i in range(len(charUsed)):
        if userLetter == charUsed[i]:
            print(f'Letter already used! Pick a different letter.\n')
            
            start(res, word, leftToFill, charUsed, incorrect, c)
    
    counter = 0        # Counter used to check if letter was in the word
    
    for i in range(len(word)):
        
        # if user's letter is in the word
        if userLetter == word[i]:
            res[i] = word[i]
            counter += 1
            leftToFill -= 1
    
    # Add letter to list of chars used
    charUsed.append(userLetter)
    
    # print word outline
    result = str(res).replace(","," ").replace("["," ").replace("]","").replace("'","")
    print(f'{result}\n')
    
    # if letter not correct decrease chances
    if counter < 1:
        incorrect += userLetter
        c -= 1
    
    # Draws hangman on each stage of where you're at in the game
    drawMan(c)
    
    # Incorrect letters shown after 1st incorrect attempt
    if len(incorrect) > 0:
        # Takes list turns to string to remove square brackets and quotes
        inc = str(incorrect).replace("[","").replace("]"," ").replace("'","")
        print(f'Incorrect letters: {inc}\n')
    
    # If game is won
    if leftToFill == 0:
        print(f'Congrats you won! You guessed the right word: {word}!\n')
        answer = str(input(f'Play again? y/yes OR n/no \n'))
        answer = answer.lower()
        
        retry(answer)
        
    # Else if game is lost
    elif c == 0:
        print(f'You lose! The correct word was: {word}\n')
        answer = str(input(f'Retry game? y/yes OR n/no \n'))
        answer = answer.lower()
        
        retry(answer)
    
    start(res, word, leftToFill, charUsed, incorrect, c)
    
def drawMan(c):
    ''' Draws the hangman in text format during various stages of the game. '''
    
    if c == 6:
        print(f'''      ______
     |     |
           |
           |
           |
       ____|____ ''')
    elif c == 5:
        print(f'''      ______
     |     |
    ( )    |
           |
           |
       ____|____ ''') 
    elif c == 4:
        print(f'''      ______
     |     |
    ( )    |
     |     |
           |
       ____|____ ''') 
    elif c == 3:
        print(f'''      ______
     |     |
    ( )    |
     |     |
    /      |
       ____|____ ''') 
    elif c == 2:
        print(f'''      ______
     |     |
    ( )    |
     |     |
    / \    |
       ____|____ ''') 
    elif c == 1:
        print(f'''      ______
     |     |
    ( )    |
    /|     |
    / \    |
       ____|____ ''') 
    else:
        print(f'''      ______
     |     |
    ( )    |
    /|\    |
    / \    |
       ____|____ ''')
    
def retry(answer):
    ''' Allows player to play another game if won or lost. '''
    
    if answer == 'y' or answer == 'yes':
        print('')
        main()
        
    elif answer == 'n' or answer == 'no':
        raise SystemExit
        
    else:
        answer = str(input('\nIncorrect input. Type either: y, yes, or n, no.\n'))
        answer = answer.lower()
        retry(answer)

def main():
    ''' Prints welcome message and begins game of Hangman. '''
    
    print("Welcome to Hangman!\nTry to guess the word!")
    getWord()
    
main()
