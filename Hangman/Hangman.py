#This program was solely written by Swetha Anbarasan
#Hangman program
import string
import random

def isWordGuessed(secretWord, lettersGuessed):
    SUCCESS = 0
    for char in secretWord:
        i=0
        while (i<len(lettersGuessed)):
            if char == lettersGuessed[i]:
                #print "I'm here"
                SUCCESS = 1
                break
            SUCCESS = 0
            i += 1
        if SUCCESS == 0:
            return False
    return True
            

               
def getGuessedWord(secretWord, lettersGuessed):
    rem_secret_str = secretWord
    guess_str = secretWord
    for char in lettersGuessed :
        if char in secretWord:
            #genertaes the remaining letters present
            rem_secret_str = rem_secret_str.replace(char,'')
    #generates the guess string with the guessed letters
    for char in rem_secret_str:
         guess_str = guess_str.replace(char,' _ ')
    return guess_str

def getAvailableLetters(lettersGuessed):
    remletters_str = string.ascii_lowercase
    for char in lettersGuessed :
        #print char
        if char in remletters_str:
            remletters_str = remletters_str.replace(char,'')
            #print remletters_str
    return remletters_str
           
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
    
    #Compute the length of the secretWord and print it
    guess = 8
    lettersGuessed=[]
    mistakesmade = 0
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' long'
    
    while(guess != 0):
        print '-------------'
        print 'You have '+ str(guess) + ' guesses left'
        print 'Available letters:' +str(getAvailableLetters(lettersGuessed))
        letter_Guessed = raw_input('Please guess a letter: ')
        if letter_Guessed not in lettersGuessed:
            lettersGuessed += letter_Guessed
            final_guess_string = (getGuessedWord(secretWord, lettersGuessed))
            if letter_Guessed in secretWord:
                print 'Good guess: ' + str(final_guess_string)
                #print lettersGuessed
                if isWordGuessed(secretWord, lettersGuessed) == True:
                   break
            else:
                print "Oops! That letter is not in my word: " + str(final_guess_string)
                guess -= 1
            #mistakesMade +=1
        else:
            print "Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed))
    print 'Secret Word was: ' +str(secretWord)
            
    
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open('/Users/swethaanbarasan/Documents/6001x/hangman_words.txt', 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

if __name__ == '__main__':
    wordList = loadWords()
    secretWord = random.choice(wordList)
    hangman(secretWord)
    
