# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "C:/Users/User/Documents/Python_scripts/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    for letter in secretWord:
        if letter not in lettersGuessed:
            count += 1
    if count == 0:
        return True
    else:
        return False
        


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    my_guess = []
    for letter in secretWord:
        if letter in lettersGuessed:
            my_guess.append(letter)
        else:
            my_guess.append("_ ")
    correctSoFar = ''.join(my_guess)
    return correctSoFar
    
    


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    allLetters = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        allLetters.remove(letter)
    remainingLetters = ''.join(allLetters)
    return remainingLetters
        

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    loadWords()
    secretWord = chooseWord(wordlist)
    #this is the start set up - always the same
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " +str(len(secretWord)) + " letters long.")
    print("-------------")
    #rounds
    guessesLeft = 8
    #variable gets replaced in while loop, always only 1 element
    lettersGuessed = ''
    #keeps track of all lettersGuessed 
    allguesses = ''
    #test if new guess is already in lettersGuessed
    testGuessed = ''
    while isWordGuessed(secretWord, allguesses) is False:
        print("You have " + str(guessesLeft) +" guesses left.")
        print("Available letters: " + getAvailableLetters(allguesses))
        lettersGuessed = input("Please guess a letter: ")
        lettersGuessed = lettersGuessed.lower()
        allguesses += lettersGuessed
        #1st check if letter has already been guessed
        if lettersGuessed in testGuessed:     
            print("Oops! You've already guessed that letter: "+ getGuessedWord(secretWord, allguesses))
            print("------------")
        #2nd check if the letter is in secret word
        else:
            if lettersGuessed in secretWord:
                print("Good guess: "+getGuessedWord(secretWord, allguesses))
                print("------------")
            else:
                print("Oops! That letter is not in my word: " +getGuessedWord(secretWord, allguesses))
                print("------------")
                guessesLeft -= 1
        #update testGuessed for next round
        testGuessed += lettersGuessed
        #3rd stop game if word is correct or ran out of guesses
        if guessesLeft == 0:
            return print("Sorry, you ran out of guesses. The word was " +str(secretWord))
        if isWordGuessed(secretWord,allguesses) is True:
            return print("Congratulations, you won!")
    
            

    
    



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
